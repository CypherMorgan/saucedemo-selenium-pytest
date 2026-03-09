from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from config.config import USERNAME, PASSWORD


def test_logout(setup):

    driver = setup

    LoginPage(driver).login(USERNAME, PASSWORD)

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    wait = WebDriverWait(driver, 10)

    logout_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )

    logout_btn.click()

    assert "saucedemo" in driver.current_url