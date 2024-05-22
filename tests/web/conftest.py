import pytest
from selene import browser
from ebay_testing_project.utils import attach
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dotenv import load_dotenv
import os


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "122.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASS')
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{selenoid_url}",
        options=options)

    browser.config.base_url = "https://www.ebay.com/"
    browser.config.driver = driver
    browser.config.driver_options = options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
