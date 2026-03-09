from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class WaitHelper:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            timeout,
            ignored_exceptions=[StaleElementReferenceException]
        )

    def wait_for_element(self, locator):
        """
        Wait until element is visible
        """

        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            )

        except TimeoutException:
            raise Exception(f"Element not visible after wait: {locator}")

    def wait_for_clickable(self, locator):
        """
        Wait until element is clickable
        """

        try:
            return self.wait.until(
                EC.element_to_be_clickable(locator)
            )

        except TimeoutException:
            raise Exception(f"Element not clickable after wait: {locator}")

    def wait_for_presence(self, locator):
        """
        Wait until element exists in DOM
        """

        try:
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )

        except TimeoutException:
            raise Exception(f"Element not present in DOM: {locator}")