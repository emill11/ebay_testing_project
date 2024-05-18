import pytest
from selene import browser

LOGIN = "emil88337@gmail.com"
PASSWORD = "!Qwerty123!"
URL = "https://www.ebay.com/"


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 800
    browser.config.base_url = URL

    yield

    browser.quit()
