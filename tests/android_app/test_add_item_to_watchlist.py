from ebay_testing_project.pages.android_app.home_page import home_page_app
from ebay_testing_project.pages.android_app.item_page import item_page
from ebay_testing_project.pages.android_app.list_items_page import list_items_page
from ebay_testing_project.utils.swipe_utils import swipe_up, swipe_down

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, query, have, be


def test_add_item_to_watchlist():
    home_page_app.open_app()
    home_page_app.click_search_field()

    browser.element((AppiumBy.ID, 'com.ebay.mobile:id/search_src_text')).type('watch')

    home_page_app.click_search_button_app()

    # Список товаров
    list_items_page.open_item()

    # товар
    swipe_up(1)
    item_page.click_add_to_watchlist()
    # нажать на поле выбора и выбрать пункт из выпадайки
    browser.element((AppiumBy.ID, 'com.ebay.mobile:id/spinner_selection_option')).click()
    browser.element((AppiumBy.ID, 'com.ebay.mobile:id/image')).click()
    # нажать кнопку го
    item_page.pop_up_click_go_to_cart()

    # открылся добавленный товар - сохранить текст
    product_title = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[1].get(query.text).strip()

    print('текст в переменной', product_title)

    swipe_down(1)
    # нажать кнопку myeBay
    browser.element((AppiumBy.ID, 'com.ebay.mobile:id/ui_bottom_nav_menu_action_my_ebay')).click()
    #открыть Watchlist
    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("Watchlist")')).click()
    #в списке есть товар с сохраненным названием
    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{product_title}")')).should(be.visible)
