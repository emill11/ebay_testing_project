import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be
from time import sleep

from ebay_testing_project.pages.android_app.home_page import home_page_app

from ebay_testing_project.utils import swipe_utils


def test_search_item_by_category():
    home_page_app.open_app()

    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("Categories")')).click()
    swipe_utils.swipe_up(2)

    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("Computers/Tablets & Networking")')).click()
    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("3D Printers & Supplies")')).click()

    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("3D Printers")')).click()

    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("ANYCUBIC")')).click()

    browser.all((AppiumBy.ID, 'com.ebay.mobile:id/cell_collection_item'))[0].click()

    swipe_utils.swipe_up(2)

    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("ANYCUBIC")')).should(be.visible)
