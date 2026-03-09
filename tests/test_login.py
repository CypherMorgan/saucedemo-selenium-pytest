import pytest
from pages.login_page import LoginPage
from config.config import USERNAME, PASSWORD


@pytest.mark.smoke
def test_login_success(setup):

    driver = setup

    LoginPage(driver).login(USERNAME, PASSWORD)

    assert "inventory" in driver.current_url    