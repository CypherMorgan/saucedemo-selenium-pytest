from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.waits import WaitHelper
from utilities.screenshot import take_screenshot


class CheckoutPage:

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    def enter_details(self, fname, lname, zip_code):

        self.wait.wait_for_element(self.first_name).send_keys(fname)
        self.wait.wait_for_element(self.last_name).send_keys(lname)
        self.wait.wait_for_element(self.postal_code).send_keys(zip_code)

        self.wait.wait_for_element(self.continue_button).click()

    def finish_order(self):

        try:
            finish_button = self.wait.wait_for_clickable((By.ID, "finish"))
            finish_button.click()

        except Exception as e:
            take_screenshot(self.driver)
            raise Exception(f"CheckoutPage: Failed to finish order → {str(e)}")