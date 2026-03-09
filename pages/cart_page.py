from selenium.webdriver.common.by import By
from utilities.waits import WaitHelper


class CartPage:

    checkout_button = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    def checkout(self):
        self.wait.wait_for_element(self.checkout_button).click()