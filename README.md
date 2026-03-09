# SauceDemo Selenium PyTest Automation Framework

A UI automation framework built with **Python, Selenium WebDriver, and PyTest** to automate core user workflows on the SauceDemo demo ecommerce application.

The framework follows the **Page Object Model (POM)** design pattern and includes reusable utilities, structured logging, explicit waits, failure screenshots, and automated HTML test reports.

---

## Tech Stack

* Python
* Selenium WebDriver
* PyTest
* PyTest HTML Reports
* WebDriver Manager

---

## Framework Features

* Page Object Model architecture
* Explicit waits for stable element interaction
* Structured logging with run-based log files
* Unique Run ID for every test execution
* Step-level logging using decorators
* Screenshot capture on test failure
* HTML test reporting
* Modular and reusable utilities
* Smoke / regression test tagging

---

## Test Scenarios

The framework automates the main ecommerce workflow of the SauceDemo application:

* Login
* Add item to cart
* Remove item from cart
* Checkout process
* Logout

---

## Project Structure
```
saucedemo-selenium-pytest
│
├── tests
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_logout.py
│
├── pages
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── utilities
│   ├── driver_factory.py
│   ├── waits.py
│   ├── screenshot.py
│   ├── logger.py
│   ├── run_context.py
│   └── step_logger.py
│
├── config
│   └── config.py
│
├── logs
│   └── run_<RUN_ID>.log
│
├── screenshots
│
├── reports
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```
---

## Framework Execution Flow

1. PyTest discovers tests inside the `tests` folder.
2. `conftest.py` initializes the browser.
3. Page Objects interact with the UI.
4. Wait utilities ensure reliable element interaction.
5. Step decorators log test actions.
6. Logs and screenshots are captured during execution.
7. PyTest generates an HTML report after the run.

---

## Running Tests

Install dependencies:

pip install -r requirements.txt

Run all tests:

pytest

Run smoke tests only:

pytest -m smoke

Run regression suite:

pytest -m regression

---

## Test Outputs

HTML report:

reports/report.html

Execution logs:

logs/run_<RUN_ID>.log

Failure screenshots:

screenshots/

---

## Future Improvements

* Parallel test execution
* CI/CD integration (GitHub Actions)
* Cross-browser testing
* Allure reporting
* Dockerized test execution

---

## Author

QA Automation learning project built using Selenium and PyTest.
