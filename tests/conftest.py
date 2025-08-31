import os, time, pytest, allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.settings import BASE_URL, BROWSER, HEADLESS

ART_DIR = "reports/artifacts"

def _make_driver():
    if BROWSER == "chrome":
        opts = ChromeOptions()
        if HEADLESS:
            opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")

        # ✅ Selenium Manager сам подберёт совместимый драйвер для установленного Chrome
        driver = webdriver.Chrome(options=opts)
        driver.set_page_load_timeout(90)
        driver.implicitly_wait(0)
        return driver
    raise RuntimeError(f"Unsupported browser: {BROWSER}")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def driver():
    drv = _make_driver()
    yield drv
    drv.quit()

def _safe_name(name: str) -> str:
    return "".join(c if c.isalnum() or c in ("_", "-", ".") else "_" for c in name)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("driver")
        if not drv:
            return
        os.makedirs(ART_DIR, exist_ok=True)
        ts = time.strftime("%Y%m%d-%H%M%S")
        name = _safe_name(item.name)
        png_path = os.path.join(ART_DIR, f"{name}_{ts}.png")
        html_path = os.path.join(ART_DIR, f"{name}_{ts}.html")
        try:
            drv.save_screenshot(png_path)
            with open(png_path, "rb") as f:
                allure.attach(f.read(), name=f"{name}_{ts}.png", attachment_type=allure.attachment_type.PNG)
        except Exception:
            pass
        try:
            page_html = drv.page_source
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(page_html)
            allure.attach(page_html, name=f"{name}_{ts}.html", attachment_type=allure.attachment_type.HTML)
        except Exception:
            pass
