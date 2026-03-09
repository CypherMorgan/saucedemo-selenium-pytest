from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import USERNAME, PASSWORD


def test_add_and_remove_item(setup):

    driver = setup

    LoginPage(driver).login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)

    inventory.add_item()
    inventory.remove_item()

    assert True