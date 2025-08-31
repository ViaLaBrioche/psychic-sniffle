from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    LOGIN_INPUT = (By.CSS_SELECTOR, 'input[id$=":login"]')
    LOGIN_BTN   = (By.CSS_SELECTOR, 'input[id$=":loginBtn"], input[id$=":loginButton"], input[id$=":login_button"]')

    def open_login(self):
        self.open("")

    def enter_login(self, login: str):
        self.type(self.LOGIN_INPUT, login)

    def submit(self):
        self.click(self.LOGIN_BTN)
