# Application CI/CD Pipeline Summary

## Overview
The Go application's CI/CD pipeline ensures code quality, testing, and deployment to Kubernetes clusters. Bitbucket handles testing and code generation, Jenkins manages building and deployment, and the `Dockerfile` creates the Docker image used for both testing and deployment. A downstream job is triggered from the application build after a successful production deployment using Jenkins' Remote Access API. This summary clarifies when the `Dockerfile` (not the test Docker Compose file) is referenced in the pipeline.

## Components

### 1. Bitbucket Pipeline
- **Purpose**: Validates commits and pull requests (PRs) through testing and code generation.
- **Image**: `golang:1.16-alpine` with Docker support and hosting resources.
- **Steps**:
  - **Dependencies**: Installs `git`, `bash`, Protocol Buffers tools, compression libraries, and SSL libraries.
  - **Code Generation**: Runs scripts to generate Protocol Buffer (`.pb.go`) and mock (`.go`) files, commits them.
  - **Testing**:
    - Uses a test Docker Compose file (currently commented out) to run tests via a test script.
    - Enforces a minimum coverage percentage (default: 97%).
    - For PRs targeting `master`, verifies the branch is merged into `staging`.
  - **Workflows**:
    - `default`: Code generation and testing for commits.
    - `pull-requests`: Testing with branch validation.
- **Dockerfile Reference**:
  - Indirectly via the test Docker Compose file, which uses the `Dockerfile` to build the application service's image.
  - Referenced in the `Testing` step (if uncommented):
    ```yaml
    # - GIT_COMMIT=$BITBUCKET_COMMIT docker-compose -f test-docker-compose.yml up --build --abort-on-container-exit
    ```
  - The `--build` flag triggers the `Dockerfile` to build the test image.
- **Note**: Testing is disabled due to commented-out Docker Compose commands.

### 2. Docker Compose (Test Configuration)
- **Purpose**: Sets up a test environment for the application.
- **Services**:
  - `redis`: Redis instance for caching.
  - `mongo`: MongoDB instance for data storage.
  - Application service: Builds image using `Dockerfile`, runs test script, connects to Redis/MongoDB.
- **Configuration**:
  - Sets minimum coverage, Redis/MongoDB connections, and test settings (e.g., test mode, debug logging).
  - Uses a bridge network.
  - Tags the application image with a commit-based identifier.
- **Dockerfile Reference**: Explicitly via `build: context: .` in the application service, pointing to the `Dockerfile` in the project root.
- **Role**: Configures the test environment, relying on the `Dockerfile` for the application image.

### 3. Test Script
- **Purpose**: Executes tests, linting, and coverage checks within the application container.
- **Steps**:
  - **Linting**: Runs `golangci-lint` for code quality.
  - **Testing**: Executes `go test` with race detection, excluding generated files (e.g., `.pb.go`, mocks).
  - **Reports**: Generates JUnit XML and coverage reports.
  - **Coverage**: Fails if coverage is below the minimum threshold (default: 97%).
- **Dockerfile Reference**: Runs in the container built from the `Dockerfile`, leveraging its dependencies (e.g., `bash`, `golangci-lint`).
- **Role**: Ensures code quality for Bitbucket's tests.

### 4. Jenkinsfile
- **Purpose**: Builds, packages, and deploys the application to Kubernetes.
- **Agent**: Runs on a node with Go 1.17.
- **Stages**:
  - **Prerequisites**: Executes `make setup` for dependencies.
  - **Build**: Executes `make install` and `make build` to compile the application.
  - **Test (Commented Out)**: Executes `make test-ci` and `golangci-lint`, publishing JUnit results.
  - **Code Quality/Quality Gate (Commented Out)**: Runs SonarQube analysis for `master`.
  - **Package**: For `qa`, `master`, `staging`, builds/pushes Docker image to a container registry, creates a version metadata file.
  - **Deploy**: Deploys to Kubernetes via Helm (production cluster for `master`, staging cluster for `qa`/`staging`).
- **Post**: Sends Slack notifications with build status.
- **Dockerfile Reference**:
  - Directly in the `package` stage:
    ```groovy
    def customImage = docker.build("<registry>/<project>/<env>/<project>:<commit>")
    customImage.push()
    ```
  - The `docker.build` command uses the `Dockerfile` in the project root to build the image for deployment.
  - The image is used in the `deploy` stage via Helm.
- **Note**: Testing and quality checks are disabled.

### 5. Dockerfile
- **Purpose**: Builds the application Docker image for testing and deployment.
- **Image**: `golang:1.16-alpine`.
- **Steps**:
  - Installs dependencies (e.g., compilers, compression libraries, SSL libraries, `git`, `bash`).
  - Configures access for private repositories.
  - Downloads Go modules, builds binary with CGO enabled and a specific tag.
  - Exposes ports for HTTP and gRPC communication.
  - Runs the application binary as entrypoint.
- **References in Pipeline**:
  - **Bitbucket**: Indirectly via the test Docker Compose file’s `build: context: .` in the `Testing` step.
  - **Jenkins**: Directly in the `package` stage via `docker.build`.
- **Role**:
  - **Testing**: Builds the test image for Bitbucket's test Docker Compose configuration.
  - **Deployment**: Builds the deployment image for Jenkins' Kubernetes deployment.
- **Note**: Contains security considerations due to repository access configuration.

## Role of Dockerfile
- **Purpose**: Creates the application Docker image, a portable artifact for testing and deployment.
- **Bitbucket Reference**: Indirectly through the test Docker Compose file’s `build: context: .`, used in the `Testing` step (if uncommented) to build a commit-tagged image.
- **Jenkins Reference**: Directly in the `package` stage via `docker.build`, producing an environment-specific image for Kubernetes deployment.
- **Consistency**: Ensures the same environment (Go 1.16, dependencies) across testing and deployment.

## Triggering Downstream Job Across Domains
- **Requirement**: Trigger a downstream job from the application build after a successful production deployment (`master` branch).
- **Challenge**: Jobs are on different Jenkins instances, requiring cross-domain communication.
- **Solution**: Use Jenkins' Remote Access API with `curl`:
  ```groovy
  stage('deploy') {
      when { anyOf { branch 'qa'; branch 'master'; branch 'staging' } }
      agent { docker { image '<registry>/ci/cdutils' args '-v <credential-path>' } }
      steps {
          script {
              if (env.BRANCH_NAME == 'master') { env.k8scluster = 'production-cluster'; env.envi = 'production' }
              else if (env.BRANCH_NAME == 'qa') { env.k8scluster = 'staging-cluster'; env.envi = 'qa' }
              else { env.k8scluster = 'staging-cluster'; env.envi = 'staging' }
          }
          sh """
              set -x
              # Authenticate and configure deployment tools
              if helm upgrade --install --wait --timeout 5m <release-name> ./deployment --set version=<version>,image.tag=<commit> -f ./deployment/<env>-values.yaml
              then
                  echo "Deployment Successful"
              else
                  helm rollback <release-name>
                  error "Deployment Failed"
              fi
          """
          script {
              if (env.BRANCH_NAME == 'master') {
                  echo "Triggering downstream job"
                  withCredentials([usernamePassword(credentialsId: 'downstream_trigger_creds', usernameVariable: 'JENKINS_USER', passwordVariable: 'JENKINS_TOKEN')]) {
                      sh """
                          curl -X POST "<downstream-jenkins-url>/job/downstream-job/build" \
                              --user "$JENKINS_USER:$JENKINS_TOKEN"
                      """
                  }
              }
          }
      }
  }