from selenium.webdriver.common.by import By
from utilities.waits import WaitHelper
from utilities.logger import get_logger


class InventoryPage:

    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    remove_backpack = (By.ID, "remove-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WaitHelper(driver)
        self.logger = get_logger("InventoryPage")

    def add_item(self):

        self.logger.info("Adding backpack to cart")
        self.wait.wait_for_clickable(self.add_backpack).click()

    def remove_item(self):

        self.logger.info("Removing backpack from cart")
        self.wait.wait_for_clickable(self.remove_backpack).click()

    def open_cart(self):

        self.logger.info("Opening cart page")
        self.wait.wait_for_clickable(self.cart_icon).click()