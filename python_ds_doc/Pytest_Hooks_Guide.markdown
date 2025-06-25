# Pytest Hooks Guide for Test Automation

This document provides a detailed overview of Pytest hooks, focusing on their use in test automation with frameworks like Selenium and Appium. It includes explanations, use cases, and sample code, with a special emphasis on the `pytest_runtest_makereport` and `pytest_runtest_logreport` hooks as used in your provided example. The guide is tailored for automation engineers working on web or mobile testing.

## Table of Contents
1. [Introduction to Pytest Hooks](#introduction-to-pytest-hooks)
2. [Key Pytest Hooks](#key-pytest-hooks)
   - [Test Collection Hooks](#test-collection-hooks)
   - [Test Setup Hooks](#test-setup-hooks)
   - [Test Execution Hooks](#test-execution-hooks)
   - [Test Reporting Hooks](#test-reporting-hooks)
   - [Test Session Teardown Hooks](#test-session-teardown-hooks)
   - [Command-Line Option Hooks](#command-line-option-hooks)
   - [Fixture-Related Hooks](#fixture-related-hooks)
3. [Detailed Analysis of Your Example](#detailed-analysis-of-your-example)
   - [`pytest_runtest_makereport`](#pytest_runtest_makereport)
   - [`pytest_runtest_logreport`](#pytest_runtest_logreport)
4. [Best Practices](#best-practices)
5. [Conclusion](#conclusion)

## Introduction to Pytest Hooks
Pytest hooks are Python functions with predefined names that allow customization of the Pytest test execution lifecycle. They are typically defined in a `conftest.py` file or a custom plugin and are used to:
- Modify test collection or execution behavior.
- Customize setup/teardown processes.
- Enhance reporting (e.g., attach screenshots in Selenium/Appium tests).
- Add custom command-line options or logging.

Hooks are particularly useful in automation testing for managing WebDriver instances, logging test results, or integrating with reporting tools like Allure.

## Key Pytest Hooks
Below are the most commonly used Pytest hooks, organized by their role in the test lifecycle, with explanations and sample code tailored for Selenium/Appium automation.

### Test Collection Hooks
These hooks are invoked during test discovery and collection.

#### `pytest_collection_modifyitems(session, config, items)`
- **Purpose**: Modify or filter the list of collected tests before execution.
- **Use Case**: Reorder tests, skip specific tests, or add custom markers for Selenium/Appium tests.
- **Example**: Skip tests marked with `@pytest.mark.mobile` unless `--platform=android` is provided.
  ```python
  def pytest_collection_modifyitems(config, items):
      if not config.getoption("--platform") == "android":
          items[:] = [item for item in items if "mobile" not in item.keywords]
  ```
- **Explanation**: This hook filters out tests marked with `mobile` if the `--platform` option isn’t set to `android`, useful for Appium tests targeting specific platforms.

#### `pytest_ignore_collect(path, config)`
- **Purpose**: Prevent collection of tests from specific files or directories.
- **Use Case**: Exclude legacy test suites or non-test files.
- **Example**:
  ```python
  def pytest_ignore_collect(path, config):
      return "deprecated" in str(path)  # Ignore files in 'deprecated' folder
  ```
- **Explanation**: This hook skips collecting tests from directories containing "deprecated", reducing clutter in large projects.

### Test Setup Hooks
These hooks run before test execution or fixture initialization.

#### `pytest_configure(config)`
- **Purpose**: Perform global configuration setup when Pytest starts.
- **Use Case**: Register custom markers or set global variables (e.g., browser type for Selenium).
- **Example**:
  ```python
  def pytest_configure(config):
      config.addinivalue_line("markers", "ui: mark tests requiring a browser")
  ```
- **Explanation**: Registers a custom `ui` marker for Selenium tests, allowing selective execution with `pytest -m ui`.

#### `pytest_sessionstart(session)`
- **Purpose**: Initialize resources before test collection.
- **Use Case**: Set up a global Selenium WebDriver or Appium driver.
- **Example**:
  ```python
  from selenium import webdriver
  def pytest_sessionstart(session):
      session.webdriver = webdriver.Chrome()  # Global WebDriver instance
  ```
- **Explanation**: Initializes a Chrome WebDriver for use across all tests, shared via the `session` object.

### Test Execution Hooks
These hooks are called during test execution.

#### `pytest_runtest_setup(item)`
- **Purpose**: Run setup logic before an individual test.
- **Use Case**: Skip tests based on conditions or navigate to a URL in Selenium.
- **Example**:
  ```python
  def pytest_runtest_setup(item):
      if "ui" in item.keywords and not item.config.getoption("--browser"):
          pytest.skip("Test requires browser but --browser not provided")
  ```
- **Explanation**: Skips UI tests if no browser is specified via a custom `--browser` option.

#### `pytest_runtest_call(item)`
- **Purpose**: Execute logic just before the test function runs.
- **Use Case**: Log test start time or modify test parameters.
- **Example**:
  ```python
  def pytest_runtest_call(item):
      print(f"Starting test: {item.nodeid}")
  ```
- **Explanation**: Logs the test’s `nodeid` before execution, useful for debugging test order.

#### `pytest_runtest_teardown(item, nextitem)`
- **Purpose**: Run teardown logic after an individual test.
- **Use Case**: Clean up resources like closing a browser window.
- **Example**:
  ```python
  def pytest_runtest_teardown(item, nextitem):
      if hasattr(item, "webdriver"):
          item.webdriver.quit()
  ```
- **Explanation**: Closes the WebDriver instance after each test to prevent resource leaks.

### Test Reporting Hooks
These hooks customize test result reporting.

#### `pytest_runtest_makereport(item, call)`
- **Purpose**: Create or modify the test report during setup, call, or teardown phases.
- **Use Case**: Attach metadata (e.g., Selenium screenshots) to reports for tools like `pytest-html` or Allure.
- **Example** (from your code):
  ```python
  def pytest_runtest_makereport(item, call):
      if call.when == "call" and call.excinfo is not None:
          '''Get the driver fixture value from the test item'''
          driver = item.funcargs.get("invoke_driver")
          if driver is not None:
              '''Attach the screenshot to the test report'''
              allure.attach(driver.get_screenshot_as_png(), name=item.nodeid, attachment_type=allure.attachment_type.PNG)
  ```
- **Explanation**:
  - **When**: Triggered only during the `call` phase (main test execution) and when an exception occurs (`call.excinfo is not None`), indicating a test failure.
  - **Action**: Retrieves the `invoke_driver` fixture (a Selenium/Appium driver) from `item.funcargs`.
  - **Outcome**: Attaches a screenshot to the Allure report with the test’s `nodeid` as the name, aiding debugging of UI/mobile test failures.
  - **Use Case**: Essential for visual debugging in Selenium/Appium when tests fail, integrating with Allure for rich reporting.

#### `pytest_runtest_logreport(report)`
- **Purpose**: Process the test report after it’s generated for logging or external integration.
- **Use Case**: Log test outcomes, send results to external systems, or capture additional debug info.
- **Example** (based on your commented code):
  ```python
  import os
  def pytest_runtest_logreport(report):
      print("AIO Report Generation")
      if report.when == 'call':
          if report.passed:
              result = 'Passed'
          elif report.failed:
              result = 'Failed'
          else:
              result = 'Skipped'
          keys = list(report.keywords.keys())
          test_cases = [item for item in keys if 'QE_TC' in item]
          for case in test_cases:
              test_case = case.replace("_", "-")
              test_cycle_key = os.environ.get('cycleKey', 'default_cycle_id')
              print(f"Updating {test_case} with status {result} in cycle {test_cycle_key}")
  ```
- **Explanation**:
  - **When**: Triggered for each test phase (setup, call, teardown), but the logic focuses on the `call` phase.
  - **Action**: Determines the test outcome (`Passed`, `Failed`, or `Skipped`) and identifies test cases marked with `QE_TC` markers.
  - **Outcome**: Simulates updating test case statuses in an external system (e.g., AIO) by replacing underscores with hyphens in test case names and using a `test_cycle_key` from environment variables.
  - **Use Case**: Useful for integrating test results with external test management systems like AIO, Jira, or TestRail in Selenium/Appium projects.

### Test Session Teardown Hooks
These hooks run after all tests complete.

#### `pytest_sessionfinish(session, exitstatus)`
- **Purpose**: Perform cleanup after the entire test session.
- **Use Case**: Close global resources like a Selenium WebDriver.
- **Example**:
  ```python
  def pytest_sessionfinish(session, exitstatus):
      if hasattr(session, "webdriver"):
          session.webdriver.quit()
  ```
- **Explanation**: Ensures the global WebDriver is closed, preventing resource leaks in Selenium tests.

#### `pytest_unconfigure(config)`
- **Purpose**: Final cleanup when Pytest exits.
- **Use Case**: Log session completion or release resources.
- **Example**:
  ```python
  def pytest_unconfigure(config):
      print("Pytest session completed")
  ```
- **Explanation**: Logs a message to confirm the test session has ended.

### Command-Line Option Hooks
These hooks customize CLI options.

#### `pytest_addoption(parser)`
- **Purpose**: Add custom command-line options.
- **Use Case**: Specify browser type or Appium platform.
- **Example**:
  ```python
  def pytest_addoption(parser):
      parser.addoption("--browser", default="chrome", help="Browser for tests")
  ```
- **Explanation**: Adds a `--browser` option to select the browser for Selenium tests, accessible via `config.getoption("--browser")`.

### Fixture-Related Hooks
These hooks customize fixture behavior.

#### `pytest_generate_tests(metafunc)`
- **Purpose**: Dynamically generate test cases based on parameters.
- **Use Case**: Run tests across multiple browsers or devices.
- **Example**:
  ```python
  def pytest_generate_tests(metafunc):
      if "browser" in metafunc.fixturenames:
          metafunc.parametrize("browser", ["chrome", "firefox"])
  ```
- **Explanation**: Parametrizes tests to run with both Chrome and Firefox, ideal for cross-browser testing in Selenium.

## Detailed Analysis of Your Example
Your provided code uses `pytest_runtest_makereport` and includes a commented-out `pytest_runtest_logreport`. Below is a detailed breakdown.

### `pytest_runtest_makereport`
**Your Code**:
```python
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        '''Get the driver fixture value from the test item'''
        driver = item.funcargs.get("invoke_driver")
        if driver is not None:
            '''Attach the screenshot to the test report'''
            allure.attach(driver.get_screenshot_as_png(), name=item.nodeid, attachment_type=allure.attachment_type.PNG)
```
- **Purpose**: Attaches a screenshot to the Allure report when a test fails during the `call` phase.
- **Breakdown**:
  - **Condition**: Checks if the phase is `call` and if an exception occurred (`call.excinfo is not None`), indicating a test failure.
  - **Driver Access**: Retrieves the `invoke_driver` fixture (a Selenium/Appium driver) from `item.funcargs`.
  - **Action**: Uses `allure.attach` to add the screenshot as a PNG attachment, named with the test’s `nodeid` (e.g., `test_file.py::test_function`).
- **Use Case**: Enhances debugging by providing visual evidence of UI/mobile app state on test failure.
- **Improvement Suggestion**:
  - Use `@pytest.hookimpl(hookwrapper=True)` to ensure compatibility with other plugins modifying the report.
  - Example:
    ```python
    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        outcome = yield
        report = outcome.get_result()
        if report.when == "call" and report.failed:
            driver = item.funcargs.get("invoke_driver")
            if driver:
                allure.attach(driver.get_screenshot_as_png(), name=report.nodeid, attachment_type=allure.attachment_type.PNG)
    ```

### `pytest_runtest_logreport`
**Your Commented Code**:
```python
def pytest_runtest_logreport(report):
    print("AIO Report Generation Skipping")
    # if report.when == 'call':
    #     if report.passed:
    #         result = 'Passed'
    #     elif report.failed:
    #         result = 'Failed'
    #     else:
    #         result = 'Skipped'
    #     keys = list(report.keywords.keys())
    #     test_cases = [item for item in keys if 'QE_TC' in item]
    #     for case in test_cases:
    #         test_case = case.replace("_", "-")
    #         if os.environ.get('cycleKey') is not None:
    #             test_cycle_key = os.environ.get('cycleKey')
    #         else:
    #             test_cycle_key = envUtil.getEnvProperty(envUtil.EnvConstants.AIO_TEST_CYCLE_ID)
    #         status = updateTestCaseStatus(test_cycle_key, test_case, result)
    #         if status in [200, 201]:
    #             print(f'{test_case} status {result} is updated in aio')
    #         else:
    #             print(f'failed to update {test_case} status {result} is updated in aio')
    #     print("Done")
```
- **Purpose**: Processes test outcomes to update statuses in an external system (AIO) for tests marked with `QE_TC` markers.
- **Breakdown**:
  - **Condition**: Focuses on the `call` phase to process test outcomes (`Passed`, `Failed`, `Skipped`).
  - **Test Case Identification**: Filters markers containing `QE_TC` (e.g., `@pytest.mark.QE_TC_123`).
  - **Action**: Converts marker names to a format with hyphens (e.g., `QE-TC-123`) and updates the test status in AIO using a `test_cycle_key` from environment variables or a utility function.
  - **Outcome**: Logs success or failure of the status update based on the HTTP response code.
- **Use Case**: Integrates test results with a test management system, useful for tracking Selenium/Appium test outcomes in CI/CD pipelines.
- **Improvement Suggestion**:
  - Handle exceptions for robustness (e.g., network errors in `updateTestCaseStatus`).
  - Use a logging framework instead of `print` for production-grade logging.
  - Example (improved):
    ```python
    import logging
    import os
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def pytest_runtest_logreport(report):
        if report.when == 'call':
            result = 'Passed' if report.passed else 'Failed' if report.failed else 'Skipped'
            test_cases = [key for key in report.keywords if 'QE_TC' in key]
            for case in test_cases:
                test_case = case.replace("_", "-")
                test_cycle_key = os.environ.get('cycleKey', 'default_cycle_id')
                try:
                    status = updateTestCaseStatus(test_cycle_key, test_case, result)
                    logger.info(f"{test_case} status {result} updated in AIO: {status}")
                except Exception as e:
                    logger.error(f"Failed to update {test_case} status {result} in AIO: {e}")
    ```

## Best Practices
1. **Use Specific Hooks**:
   - Use `pytest_runtest_makereport` for modifying reports (e.g., attaching screenshots).
   - Use `pytest_runtest_logreport` for post-report actions like logging or external integration.
2. **Keep Hooks Lightweight**:
   - Avoid heavy operations in hooks to maintain test performance.
3. **Leverage Fixtures**:
   - Access Selenium/Appium drivers via `item.funcargs` or fixtures for context-specific actions.
4. **Integrate with Reporting Tools**:
   - Combine hooks with Allure or `pytest-html` for rich reporting (e.g., screenshots, logs).
5. **Handle Errors Gracefully**:
   - Use try-except blocks in hooks to prevent test session crashes.
6. **Test Hooks**:
   - Run with `pytest -s -v` to verify hook behavior via logs.

## Conclusion
Pytest hooks provide powerful customization for test automation, especially in Selenium and Appium projects. The `pytest_runtest_makereport` hook is ideal for modifying test reports (e.g., attaching screenshots to Allure), while `pytest_runtest_logreport` excels at logging or integrating results with external systems like AIO. By combining these with other hooks like `pytest_addoption` or `pytest_generate_tests`, you can build a robust automation framework tailored to your needs.

For further customization, share specific requirements (e.g., additional reporting needs or test management integrations), and I can provide more tailored hook implementations.