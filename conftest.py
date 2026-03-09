import logging
import pytest
from utilities.driver_factory import get_driver
from config.config import BASE_URL
from utilities.screenshot import take_screenshot


@pytest.fixture(scope="function")
def setup(request):

    driver = get_driver()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["setup"]
        take_screenshot(driver)

def pytest_runtest_logreport(report):

    if report.when == "call":
        logging.info(f"Test {report.nodeid} finished with status: {report.outcome}")