from selenium.webdriver.common.by import By
from utilities.waits import WaitHelper
from utilities.logger import get_logger


class LoginPage:

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WaitHelper(driver)
        self.logger = get_logger("LoginPage")

    def login(self, username, password):

        self.logger.info("Entering username")
        self.wait.wait_for_element(self.username).send_keys(username)

        self.logger.info("Entering password")
        self.wait.wait_for_element(self.password).send_keys(password)

        self.logger.info("Clicking login button")
        self.wait.wait_for_clickable(self.login_button).click()