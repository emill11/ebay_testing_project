import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class HomePageApp:
    def open_app(self):
        with allure.step('Открыть приложение'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, "eBay")).click()

    def click_search_field(self):
        with allure.step('Нажать на поле ввода'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Keyword Search on eBay')).click()

    def fill_search_field(self):
        with allure.step('Заполнить поле ввода'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/search_src_text')).type('headphones')

    def сlick_item_in_drop_down(self):
        with allure.step('Нажать на первый пункт выпадайки'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/search_suggestion_text')).click()

    def click_categories(self):
        with allure.step('Нажать кнопку Categories'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("Categories")')).click()


home_page_app = HomePageApp()
