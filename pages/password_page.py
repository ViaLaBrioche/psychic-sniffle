from selenium.webdriver.common.by import By
from .base_page import BasePage

class PasswordPage(BasePage):
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#password_common, input[id$=":password_common"]')
    SUBMIT_BTN     = (By.CSS_SELECTOR, 'input#loginButton, input[id$=":loginButton"]')

    def enter_password(self, password: str):
        self.type(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click(self.SUBMIT_BTN)
