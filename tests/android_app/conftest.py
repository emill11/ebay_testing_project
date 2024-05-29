import pytest
from selene import browser
from ebay_testing_project.utils import attach
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
import os
import allure

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    url = os.getenv('APPIUM_SERVER_URL')

    options = UiAutomator2Options()
    options.set_capability('remote_url', url)
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")

    browser.config.driver = webdriver.Remote(url, options=options)
    browser.config.timeout = 10.0

    yield

    with allure.step('Добавить скриншот'):
        attach.mobile_attach_screen(browser)

    with allure.step('Добавить xml'):
        attach.mobile_attach_xml(browser)

    browser.driver.terminate_app('com.ebay.mobile')
