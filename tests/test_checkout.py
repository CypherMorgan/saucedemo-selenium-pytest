from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import USERNAME, PASSWORD


def test_checkout_process(setup):

    driver = setup

    LoginPage(driver).login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_item()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_details("John", "Doe", "10001")
    checkout.finish_order()

    assert "checkout-complete" in driver.current_url