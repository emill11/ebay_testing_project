from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
import allure


class MyEbayPage():
    def my_ebay_button_click(self):
        with allure.step('В нижней панели нажать My eBay'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/ui_bottom_nav_menu_action_my_ebay')).click()

    def watchlist_button_click(self):
        with allure.step('Нажать на пункт Watchlist'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("Watchlist")')).click()

    def click_recently_viewed(self):
        with allure.step('Нажать на пункт Recently viewed'):
            browser.element((AppiumBy.XPATH, "//android.widget.TextView[@text='Recently viewed']")).click()


my_ebay_page = MyEbayPage()
