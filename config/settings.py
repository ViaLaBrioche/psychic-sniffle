import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://mb1.bbr.ru")
BROWSER = os.getenv("BROWSER", "chrome")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "15"))

AFTER_LOGIN_URL_CONTAINS = os.getenv("AFTER_LOGIN_URL_CONTAINS", "/protected/")
AFTER_LOGIN_ASSERT_CSS = os.getenv("AFTER_LOGIN_ASSERT_CSS", "")

TESTDATA = {
    "users": {
        "valid": {
            "username": os.getenv("UI_USER", ""),
            "password": os.getenv("UI_PASS", ""),
        }
    }
}
