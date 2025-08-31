import pytest, allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.password_page import PasswordPage
from utils.assertions import wait_visible_css
from config.settings import TESTDATA, AFTER_LOGIN_URL_CONTAINS, AFTER_LOGIN_ASSERT_CSS

@allure.feature("Auth")
@allure.story("Successful login")
@pytest.mark.e2e
def test_success_login_and_home_asserts(driver, base_url):
    username = TESTDATA["users"]["valid"]["username"]
    password = TESTDATA["users"]["valid"]["password"]
    assert username and password, "UI_USER/UI_PASS не заданы в окружении"

    with allure.step("Open login page and submit username"):
        lp = LoginPage(driver, base_url)
        lp.open_login()
        lp.enter_login(username)
        lp.submit()

    with allure.step("Enter password and submit"):
        pp = PasswordPage(driver, base_url)
        assert pp.is_visible(PasswordPage.PASSWORD_INPUT, timeout=15), "Не появилась форма ввода пароля"
        pp.enter_password(password)
        pp.submit()

    with allure.step("Assert redirected URL and main element visible"):
        WebDriverWait(driver, 25).until(EC.url_contains(AFTER_LOGIN_URL_CONTAINS))
        assert AFTER_LOGIN_URL_CONTAINS in driver.current_url, (
            f"Ожидали '{AFTER_LOGIN_URL_CONTAINS}' в URL, но получили: {driver.current_url}"
        )
        if AFTER_LOGIN_ASSERT_CSS:
            wait_visible_css(driver, AFTER_LOGIN_ASSERT_CSS, timeout=20)
        else:
            pytest.skip("AFTER_LOGIN_ASSERT_CSS не задан. Укажи конкретный CSS для проверки главной.")
