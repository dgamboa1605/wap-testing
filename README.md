# Test Automation Framework WAP-testing

## Overview
This framework is designed for automating UI tests using Selenium WebDriver with Pytest. It supports multiple browsers (Chrome, Firefox, and Edge) and is structured to provide clean, maintainable, and scalable code, following the Page Object Model (POM) pattern.

### Key Features:
- Multi-browser support (Chrome, Firefox, Edge).
- Configurable browser options and implicit/explicit waits.
- Integrated logging for debugging.
- Allure reporting for test results.
- Clean code following best practices (POM, utility classes, logger).
- Easy extension to add new pages and tests.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:dgamboa1605/wap-testing.git
   cd wap-testing
   ```

2. **Install the required dependencies**:
   Make sure you have Python installed. Then, use pip to install the necessary packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Allure Report Setup**:
   Install Allure to generate and visualize test reports:
   - [Allure Commandline Installation Guide](https://docs.qameta.io/allure/#_installing_a_commandline)

---

## Framework Structure

```
wap-testing
│
├── config/
│   └── config.py        # Configuration settings (e.g., browser, URL, waits, logging)
│
├── drivers/
│   ├── browser_factory.py  # Browser factory for handling multiple browsers
│   ├── chrome_browser.py   # Chrome browser setup
│   ├── firefox_browser.py  # Firefox browser setup
│   └── edge_browser.py     # Edge browser setup
│
├── pages/
│   ├── base_page.py     # Base class for common page actions
│   ├── home_page.py     # Page object for the Home Page
│   ├── search_page.py   # Page object for the Search Page
│   └── streamer_page.py # Page object for the Streamer Page
│
├── tests/
│   ├── conftest.py      # Pytest fixtures
│   └── test_search_page.py  # Test cases for search functionality
│
├── utilities/
│   ├── logger.py        # Logger utility
│   └── utils.py         # Utility functions
│
├── logs/                # Directory to store logs
├── reports/             # Directory for Allure reports
├── pytest.ini           # Pytest configuration file
└── requirements.txt     # Required Python packages
```

---

## Running Tests

1. **Basic Test Execution**:
   To execute all tests, run the following command:
   ```bash
   pytest
   ```

2. **Running Tests with Allure Reporting**:
   Run the tests and generate Allure reports:
   ```bash
   pytest --alluredir=reports
   ```

   After the test run, serve the report using:
   ```bash
   allure serve reports
   ```

3. **Running Tests in Parallel**:
   Execute tests across multiple cores to reduce execution time:
   ```bash
   pytest -n auto
   ```

4. **Browser-Specific Execution**:
   The browser can be changed via the `config/config.py` file by setting the `BROWSER` variable to either `chrome`, `firefox`, or `edge`.

---

## Linting and Code Quality

To ensure code quality, the framework uses `pylint` to analyze Python code. To run pylint, use the following command:
```bash
pylint <path_to_your_python_files>
```

---

## Adding Tests

1. **Create a new test file** under the `tests/` directory (e.g., `test_new_feature.py`).
2. **Write your test cases** using Pytest.
3. **Use the page objects** to interact with the web elements.
   Example:
   ```python
   from pages.home_page import HomePage

   def test_example(browser):
       home_page = HomePage(browser)
       home_page.click_on_search()
   ```

---

## Continuous Integration/Continuous Deployment (CI/CD) Integration

In the future, this framework can be integrated into CI/CD pipelines such as Jenkins, GitLab CI, or GitHub Actions by:
- Setting up a job to install dependencies (`pip install -r requirements.txt`).
- Running tests using `pytest` with reporting (`pytest --alluredir=reports`).
- Generating Allure reports post-execution.

Example CI step:
```yaml
stages:
  - lint
  - test

lint:
  stage: lint
  script:
    - pylint pages/

test_job:
  stage: test
  script:
    - pip install -r requirements.txt
    - pytest --alluredir=reports
  artifacts:
    when: always
    paths:
      - reports/
```

---

## Future Improvements

- **Integrate with CI/CD pipelines** for automated execution.
- **Add Docker support** to easily manage dependencies and execution environments.
- **Extend browser options** for running tests on cloud services like Selenium Grid or BrowserStack.

---
