from selenium.webdriver.common.by import By
from utilities.waits import WaitHelper
from utilities.step_logger import log_step


class InventoryPage:

    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    remove_backpack = (By.ID, "remove-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WaitHelper(driver)


    @log_step("Adding backpack to cart")
    def add_item(self):

        self.wait.wait_for_clickable(self.add_backpack).click()


    @log_step("Removing backpack from cart")
    def remove_item(self):

        self.wait.wait_for_clickable(self.remove_backpack).click()


    @log_step("Opening cart page")
    def open_cart(self):

        self.wait.wait_for_clickable(self.cart_icon).click()