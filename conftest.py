import logging
import os
import pytest

from config.config import BASE_URL
from utilities.driver_factory import get_driver
from utilities.screenshot import take_screenshot
from utilities.run_context import RUN_ID


# Configure logging immediately when pytest loads this file
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, f"run_{RUN_ID}.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)


def pytest_sessionstart(session):

    logging.info("=====================================")
    logging.info(f"TEST RUN STARTED | RUN_ID: {RUN_ID}")
    logging.info("=====================================")


def pytest_sessionfinish(session, exitstatus):

    logging.info("=====================================")
    logging.info("TEST RUN FINISHED")
    logging.info("=====================================")


@pytest.fixture(scope="function")
def setup():

    driver = get_driver()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup")

        if driver:
            take_screenshot(driver, item.name)


def pytest_runtest_logstart(nodeid, location):
    logging.info(f"START TEST: {nodeid}")


def pytest_runtest_logfinish(nodeid, location):
    logging.info(f"END TEST: {nodeid}")


def pytest_runtest_logreport(report):

    if report.when == "call":
        logging.info(
            f"RESULT | {report.nodeid} | STATUS: {report.outcome.upper()}"
        )