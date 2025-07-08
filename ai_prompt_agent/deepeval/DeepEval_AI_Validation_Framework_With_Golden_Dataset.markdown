# DeepEval-Based Framework for AI Application Validation with Custom Metrics and Golden Datasets

This document provides an in-depth explanation of creating custom metrics in DeepEval, the differences between `GEval` and `BaseMetric`, and the concept and creation of golden datasets. It also presents a tailored framework for validating AI applications where the input is a job search query, and the expected output is a list of matching jobs, using JSONL test data, API-driven actual outputs, and a custom metric for job-user similarity.

## Part 1: Understanding Custom Metrics in DeepEval

### 1.1 Creating a Custom Metric

In DeepEval, custom metrics allow you to define evaluation logic tailored to your specific use case. You can create custom metrics by extending either `GEval` or `BaseMetric`, depending on whether you want an LLM-based or deterministic evaluation.

#### Steps to Create a Custom Metric
1. **Choose the Base Class**: Decide between `GEval` (LLM-based) or `BaseMetric` (deterministic).
2. **Implement Required Methods**:
   - For `BaseMetric`: Implement `measure`, `a_measure` (async version), and `is_successful`.
   - For `GEval`: Define `evaluation_steps` and `evaluation_params`.
3. **Define Measurement Logic**: Specify how the metric evaluates the test case (e.g., similarity score, rule-based check).
4. **Test the Metric**: Validate in a separate test file (e.g., `test_custom_metrics.py`).

#### `GEval` vs. `BaseMetric`

**`GEval`**:
- **Purpose**: Uses an LLM (e.g., GPT-4, Mistral-7B) as a judge to evaluate outputs based on qualitative criteria.
- **When to Use**: Suitable for subjective evaluations (e.g., tone, politeness, creativity) where human-like judgment is needed.
- **Class to Extend**: `GEval` (inherits from `BaseMetric` but is pre-configured for LLM-based evaluation).
- **How DeepEval Understands Measurement Logic**:
  - You define `evaluation_steps` (a list of instructions for the LLM to follow).
  - You specify `evaluation_params` (test case fields like `input`, `actual_output`, `expected_output`, `context`).
  - DeepEval sends these to the LLM, which returns a score (0–1) and a reason based on the steps.
- **Pros**:
  - Flexible for complex, subjective evaluations.
  - Leverages LLM reasoning for nuanced judgments.
- **Cons**:
  - Stochastic (results may vary due to LLM variability).
  - Requires API access or local LLM setup, increasing cost or complexity.
- **Example**:
  ```python
  from deepeval.metrics import GEval
  from deepeval.test_case import LLMTestCaseParams

  class PolitenessMetric(GEval):
      def __init__(self, threshold: float = 0.8):
          super().__init__(
              name="Politeness",
              evaluation_steps=[
                  "Check if the response uses polite language (e.g., 'please', 'thank you').",
                  "Ensure the tone is professional and respectful."
              ],
              evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
              threshold=threshold,
              model="mistral-7b"  # Open-source LLM
          )
  ```
  - **Measurement Logic**: The LLM evaluates the `actual_output` based on the defined steps, assigning a score for politeness.

**`BaseMetric`**:
- **Purpose**: Allows fully deterministic, rule-based evaluations without relying on an LLM.
- **When to Use**: Suitable for objective evaluations (e.g., format validation, numerical similarity, regex checks).
- **Class to Extend**: `BaseMetric` (base class for all DeepEval metrics).
- **How DeepEval Understands Measurement Logic**:
  - You implement the `measure` method to define custom logic (e.g., compute a similarity score).
  - The `a_measure` method provides an async version for compatibility.
  - The `is_successful` method determines if the score meets the threshold.
  - DeepEval uses your logic to compute a score (0–1) and success status.
- **Pros**:
  - Deterministic and consistent results.
  - No LLM dependency, reducing cost and latency.
- **Cons**:
  - Requires manual coding of evaluation logic.
  - Less flexible for subjective or complex evaluations.
- **Example**:
  ```python
  from deepeval.metrics import BaseMetric
  import json

  class JSONFormatMetric(BaseMetric):
      def __init__(self, threshold: float = 0.9):
          self.threshold = threshold
          self.name = "JSONFormat"

      def measure(self, test_case):
          try:
              json.loads(test_case.actual_output)
              self.score = 1.0
              self.success = True
          except json.JSONDecodeError:
              self.score = 0.0
              self.success = False
          return self.score

      async def a_measure(self, test_case):
          return self.measure(test_case)

      def is_successful(self):
          return self.success
  ```
  - **Measurement Logic**: The metric checks if `actual_output` is valid JSON, assigning a score of 1.0 for valid JSON and 0.0 otherwise.

#### Choosing Between `GEval` and `BaseMetric`
- Use `GEval` for:
  - Subjective evaluations (e.g., tone, intent, user satisfaction).
  - Cases where LLM reasoning can simplify complex criteria.
- Use `BaseMetric` for:
  - Objective, rule-based checks (e.g., format validation, similarity scores).
  - Scenarios requiring consistency and low latency.
- For your job-user similarity metric, use `BaseMetric` since it involves computing a deterministic cosine similarity score using embeddings.

### 1.2 Custom Metric: JobUserSimilarityMetric

This metric evaluates the similarity between a job description and a user profile using embeddings from `sentence-transformers`.

**Implementation**:
```python
# metrics/custom_metrics.py
from deepeval.metrics import BaseMetric
from sentence_transformers import SentenceTransformer, util

class JobUserSimilarityMetric(BaseMetric):
    def __init__(self, threshold: float = 0.8, model_name: str = "all-MiniLM-L6-v2"):
        self.threshold = threshold
        self.name = "JobUserSimilarity"
        self.model = SentenceTransformer(model_name)

    def measure(self, test_case):
        # Extract job description and user profile from context
        job_description = test_case.context[0] if test_case.context else ""
        user_profile = test_case.context[1] if len(test_case.context) > 1 else ""
        if not job_description or not user_profile:
            self.score = 0.0
            self.success = False
            return self.score

        # Compute embeddings
        job_embedding = self.model.encode(job_description, convert_to_tensor=True)
        user_embedding = self.model.encode(user_profile, convert_to_tensor=True)

        # Calculate cosine similarity
        similarity = util.cos_sim(job_embedding, user_embedding)[0][0].item()
        self.score = similarity
        self.success = similarity >= self.threshold
        return self.score

    async def a_measure(self, test_case):
        return self.measure(test_case)

    def is_successful(self):
        return self.success
```

**Explanation**:
- **Base Class**: Extends `BaseMetric` for deterministic evaluation.
- **Logic**: Uses `sentence-transformers` (`all-MiniLM-L6-v2`) to compute embeddings and cosine similarity between job description and user profile.
- **Threshold**: 0.8 ensures high similarity for relevant job recommendations.
- **Context**: Expects `test_case.context` to contain `[job_description, user_profile]`.
- **Use Case**: Validates that recommended jobs match user qualifications.

## Part 2: Understanding Golden Datasets

### 2.1 What is a Golden Dataset?

A golden dataset is a high-quality, curated set of test cases used as a benchmark for evaluating AI systems. Each test case includes:
- **Input**: The query or prompt (e.g., “Find a job for a Python developer”).
- **Expected Output**: The ideal response (e.g., a list of relevant jobs).
- **Context**: Additional data for evaluation (e.g., job descriptions, user profiles).
- **Ground Truth**: Optionally, annotations or labels for metrics like similarity scores.

**Significance**:
- **Benchmarking**: Provides a standard to measure model performance.
- **Consistency**: Ensures reproducible evaluations across iterations.
- **Edge Cases**: Includes diverse scenarios to test robustness.
- **Regression Testing**: Detects performance degradation in updates.

### 2.2 Creating a Golden Dataset

#### Manual Creation
- **Process**:
  1. Collect representative inputs (e.g., job search queries).
  2. Define expected outputs (e.g., lists of relevant jobs).
  3. Add context (e.g., job descriptions, user profiles).
  4. Store in JSONL format for compatibility with DeepEval.
- **Example `test_cases.jsonl`**:
  ```jsonl
  {"input": "Find a job for a software engineer with Python experience.", "expected_output": ["Software Engineer at TechCorp, Python and Django required", "Backend Developer at CodeCo, Python expertise"], "context": ["Software Engineer at TechCorp, requires 3+ years of Python, Django, and cloud experience.", "Software engineer with 4 years of Python experience, skilled in Django and AWS."]}
  {"input": "Recommend a job for a data scientist.", "expected_output": ["Data Scientist at DataCo, machine learning focus", "AI Researcher at InnovateAI, ML and R required"], "context": ["Data Scientist at DataCo, requires expertise in machine learning and R.", "Data scientist with 2 years of experience in machine learning and Python."]}
  ```

#### Synthetic Generation with DeepEval’s `Synthesizer`
- **Process**:
  1. Use `Synthesizer` to generate test cases from seed contexts.
  2. Review and refine generated cases for quality.
  3. Save to `test_cases.jsonl`.
- **Example**:
  ```python
  from deepeval.synthesize import Synthesizer
  synthesizer = Synthesizer(model="mistral-7b")
  test_cases = synthesizer.generate_goldens(
      contexts=["Job descriptions and user profiles"], 
      prompt="Generate diverse job recommendation queries",
      num_evolutions=10  # Generate 10 variations
  )
  with open("data/test_cases.jsonl", "a") as f:
      for tc in test_cases:
          f.write(json.dumps({
              "input": tc.input,
              "expected_output": tc.expected_output,
              "context": tc.context
          }) + "\n")
  ```
- **Significance**: Automates creation of diverse test cases, covering edge cases like niche roles or unqualified users.

#### Best Practices for Golden Datasets
- **Diversity**: Include varied inputs (e.g., different job roles, skill levels).
- **Quality**: Manually review synthetic data for accuracy.
- **Size**: Aim for 50–100 test cases for robust evaluation.
- **Format**: Use JSONL for scalability and compatibility with DeepEval.

## Part 3: Framework for Job Recommendation System

This framework validates an AI application where inputs are job search queries, and expected outputs are lists of matching jobs. It uses JSONL test data, API-driven actual outputs, and the custom `JobUserSimilarityMetric`.

### Project Structure
```plaintext
ai_validation_framework/
├── tests/
│   ├── test_prompts.py       # Prompt-based system tests
│   ├── test_agents.py        # Agent-based system tests
│   ├── test_custom_metrics.py # Custom metric tests
├── metrics/
│   ├── custom_metrics.py     # Custom metric definitions
├── data/
│   ├── test_cases.jsonl      # Golden dataset
├── logs/
│   ├── test.log              # Log file
├── reports/
│   ├── allure/               # Allure report output
├── config/
│   ├── config.yaml           # Configurations
├── requirements.txt           # Dependencies
├── README.md                 # Documentation
```

### Setup
```bash
pip install -U deepeval requests sentence-transformers huggingface_hub transformers lm-format-enforcer
deepeval login  # For Confident AI
```

### Configuration (`config.yaml`)
```yaml
api_endpoint: http://localhost:8000/recommend
retries: 3
timeout: 10
model: mistral-7b
embedding_model: all-MiniLM-L6-v2
```

### JSONL Test Data
**`test_cases.jsonl`**:
```jsonl
{"input": "Find a job for a software engineer with Python experience.", "expected_output": ["Software Engineer at TechCorp, Python and Django required", "Backend Developer at CodeCo, Python expertise"], "context": ["Software Engineer at TechCorp, requires 3+ years of Python, Django, and cloud experience.", "Software engineer with 4 years of Python experience, skilled in Django and AWS."]}
{"input": "Recommend a job for a data scientist.", "expected_output": ["Data Scientist at DataCo, machine learning focus", "AI Researcher at InnovateAI, ML and R required"], "context": ["Data Scientist at DataCo, requires expertise in machine learning and R.", "Data scientist with 2 years of experience in machine learning and Python."]}
```

### Implementation

#### Custom Metric
```python
# metrics/custom_metrics.py
from deepeval.metrics import BaseMetric
from sentence_transformers import SentenceTransformer, util

class JobUserSimilarityMetric(BaseMetric):
    def __init__(self, threshold: float = 0.8, model_name: str = "all-MiniLM-L6-v2"):
        self.threshold = threshold
        self.name = "JobUserSimilarity"
        self.model = SentenceTransformer(model_name)

    def measure(self, test_case):
        job_description = test_case.context[0] if test_case.context else ""
        user_profile = test_case.context[1] if len(test_case.context) > 1 else ""
        if not job_description or not user_profile:
            self.score = 0.0
            self.success = False
            return self.score

        job_embedding = self.model.encode(job_description, convert_to_tensor=True)
        user_embedding = self.model.encode(user_profile, convert_to_tensor=True)
        similarity = util.cos_sim(job_embedding, user_embedding)[0][0].item()
        self.score = similarity
        self.success = similarity >= self.threshold
        return self.score

    async def a_measure(self, test_case):
        return self.measure(test_case)

    def is_successful(self):
        return self.success
```

#### Test Script
```python
# tests/test_prompts.py
import json
import logging
import requests
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from metrics.custom_metrics import JobUserSimilarityMetric

logging.basicConfig(
    filename="logs/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s"
)

def get_actual_output(input_text, api_endpoint="http://localhost:8000/recommend", retries=3):
    for attempt in range(retries):
        try:
            response = requests.post(api_endpoint, json={"input": input_text}, timeout=10)
            response.raise_for_status()
            return response.json().get("output", [])  # Expect a list of jobs
        except requests.RequestException as e:
            logging.error(f"API request failed: {e}")
            if attempt < retries - 1:
                sleep(2)
            else:
                raise Exception(f"API request failed after {retries} attempts: {e}")

def load_test_cases(jsonl_file):
    test_cases = []
    with open(jsonl_file, 'r') as f:
        for line in f:
            data = json.loads(line.strip())
            test_case = LLMTestCase(
                input=data['input'],
                expected_output=data['expected_output'],  # List of jobs
                context=[data['context']['job_description'], data['context']['user_profile']],
                actual_output=get_actual_output(data['input'])
            )
            test_cases.append(test_case)
    return test_cases

test_cases = load_test_cases("data/test_cases.jsonl")
for test_case in test_cases:
    logging.info(f"Testing: {test_case.input}")
    metrics = [
        AnswerRelevancyMetric(threshold=0.8),
        FaithfulnessMetric(threshold=0.7),
        JobUserSimilarityMetric(threshold=0.8)
    ]
    assert_test(test_case, metrics)
```

#### Testing Custom Metric
```python
# tests/test_custom_metrics.py
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from metrics.custom_metrics import JobUserSimilarityMetric

def test_job_user_similarity():
    test_case = LLMTestCase(
        input="Find a job for a Python developer.",
        actual_output=["Software Engineer at TechCorp, Python and Django required"],
        context=[
            "Software Engineer at TechCorp, requires 3+ years of Python, Django, and cloud experience.",
            "Software engineer with 4 years of Python experience, skilled in Django and AWS."
        ]
    )
    metric = JobUserSimilarityMetric(threshold=0.8)
    assert_test(test_case, [metric])
```

### Reporting
- **Terminal**: Pass/fail status, scores (e.g., JobUserSimilarity: 0.92).
- **Allure**:
  ```python
  import allure
  def test_with_allure():
      with allure.step("Running DeepEval test"):
          test_case = load_test_cases("data/test_cases.jsonl")[0]
          metric = JobUserSimilarityMetric(threshold=0.8)
          assert_test(test_case, [metric])
          with open("logs/test.log", "r") as log_file:
              allure.attach(log_file.read(), name="Test Log", attachment_type=allure.attachment_type.TEXT)
  ```
  Run: `pytest --alluredir=reports/allure` and `allure serve reports/allure`.
- **Confident AI**: Run `deepeval test run --confident` for dashboards with metric trends.

### Best Practices
1. **Metric Selection**: Use AnswerRelevancy, Faithfulness, and JobUserSimilarityMetric.
2. **Golden Dataset**: Curate 50–100 diverse test cases, validate JSONL syntax.
3. **API Handling**: Implement retries and logging for robustness.
4. **Synthetic Data**: Use `Synthesizer` for diverse queries.
5. **CI/CD**: Integrate with GitHub Actions:
   ```yaml
   name: AI Validation
   on: [push]
   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - run: pip install -r requirements.txt
         - run: pytest tests/ --alluredir=reports/allure
         - run: deepeval test run --confident
   ```

## Conclusion

This framework leverages DeepEval to validate job recommendation systems using JSONL golden datasets, API-driven outputs, and a custom `JobUserSimilarityMetric`. `GEval` is ideal for subjective evaluations, while `BaseMetric` suits deterministic checks like similarity scores. Golden datasets ensure robust benchmarking. For further details, see [DeepEval Documentation](https://docs.confident-ai.com/docs/getting-started) or [GitHub](https://github.com/confident-ai/deepeval). For pricing, visit [xAI](https://x.ai/grok).