from selenium.webdriver.common.by import By
from utilities.waits import WaitHelper
from utilities.step_logger import log_step


class LoginPage:

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WaitHelper(driver)


    @log_step("Entering username")
    def enter_username(self, username):

        self.wait.wait_for_element(self.username).send_keys(username)


    @log_step("Entering password")
    def enter_password(self, password):

        self.wait.wait_for_element(self.password).send_keys(password)


    @log_step("Clicking login button")
    def click_login(self):

        self.wait.wait_for_clickable(self.login_button).click()


    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()