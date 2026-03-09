from selenium.webdriver.common.by import By
from utilities.waits import WaitHelper
from utilities.step_logger import log_step


class CartPage:

    checkout_button = (By.ID, "checkout")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WaitHelper(driver)


    @log_step("Clicking checkout button")
    def checkout(self):

        self.wait.wait_for_clickable(self.checkout_button).click()