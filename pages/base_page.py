from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, base_url, wait_timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.base_url = base_url

    def open(self, path=""):
        self.driver.get(self.base_url + path)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text, clear=True):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            el.clear()
        el.send_keys(text)

    def text_of(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator, timeout=None):
        from selenium.webdriver.support.ui import WebDriverWait
        try:
            WebDriverWait(self.driver, timeout or self.wait._timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False
