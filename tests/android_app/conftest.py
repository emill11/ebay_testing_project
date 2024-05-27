import pytest
from selene import browser
from ebay_testing_project.utils import attach
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    url = 'http://127.0.0.1:4723'

    options = UiAutomator2Options()
    options.set_capability('remote_url', url)
    options.set_capability("platformName", "Android")
    options.set_capability("automationName", "UiAutomator2")

    browser.config.driver = webdriver.Remote(url, options=options)
    browser.config.timeout = 10.0

    yield

    # attach.attach_screen(browser)
    # attach.attach_xml(browser)

    # browser.quit()
    # browser.driver.quit()

    browser.driver.terminate_app('com.ebay.mobile')
