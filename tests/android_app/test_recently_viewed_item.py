from ebay_testing_project.pages.android_app.home_page import home_page_app
from ebay_testing_project.pages.android_app.item_page import item_page
from ebay_testing_project.pages.android_app.list_items_page import list_items_page
from ebay_testing_project.utils.swipe_utils import swipe_up, swipe_down

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, query, be
from time import sleep


def test_recently():
    home_page_app.open_app()
    home_page_app.click_search_field()
    browser.element((AppiumBy.ID, 'com.ebay.mobile:id/search_src_text')).type('watch')
    home_page_app.click_search_button_app()

    # открыть товар
    list_items_page.open_item()

    # скопировать название
    product_title = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[2].get(query.text).strip()
    print('текст в переменной', product_title)
    #открыть мой ибэй
    browser.element((AppiumBy.ID, 'com.ebay.mobile:id/ui_bottom_nav_menu_action_my_ebay')).click()
    #открыть недавно просмотренные
    browser.element((AppiumBy.XPATH, "//android.widget.TextView[@text='Recently viewed']")).click()
    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{product_title}")')).should(be.visible)

