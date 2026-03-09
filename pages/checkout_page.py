from selenium.webdriver.common.by import By
from utilities.waits import WaitHelper
from utilities.step_logger import log_step


class CheckoutPage:

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WaitHelper(driver)


    @log_step("Entering first name")
    def enter_first_name(self, fname):

        self.wait.wait_for_element(self.first_name).send_keys(fname)


    @log_step("Entering last name")
    def enter_last_name(self, lname):

        self.wait.wait_for_element(self.last_name).send_keys(lname)


    @log_step("Entering postal code")
    def enter_postal_code(self, code):

        self.wait.wait_for_element(self.postal_code).send_keys(code)


    @log_step("Clicking continue")
    def click_continue(self):

        self.wait.wait_for_clickable(self.continue_button).click()


    @log_step("Clicking finish order")
    def finish_order(self):

        self.wait.wait_for_clickable(self.finish_button).click()


    def enter_details(self, fname, lname, zip_code):

        self.enter_first_name(fname)
        self.enter_last_name(lname)
        self.enter_postal_code(zip_code)
        self.click_continue()