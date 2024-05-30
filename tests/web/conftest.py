import pytest
from selene import browser
from ebay_testing_project.utils import attach
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from dotenv import load_dotenv
import os
import allure

load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--context", action="store", default="selenoid",
                     help="Context for load options")


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    context = request.config.getoption("--context")
    driver = None
    options = Options()

    if context == "selenoid":
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

    if context == "local":
        driver = webdriver.Chrome(options=options)

    browser.config.driver = driver
    browser.config.base_url = "https://www.ebay.com/"
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    with allure.step('Добавить скриншот'):
        attach.web_add_screenshot(browser)
    with allure.step('Добавить логи'):
        attach.web_add_logs(browser)

        # if context == "selenoid":
    with allure.step('Добавить видео'):
        attach.web_add_video(browser)

    browser.quit()
