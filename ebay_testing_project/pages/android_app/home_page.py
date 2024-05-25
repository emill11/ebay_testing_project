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
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/search_src_text')).type('jacket')

    def click_search_button_app(self):
        with allure.step('Нажать на кнопку поиска '):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/search_suggestion_text')).click()


home_page_app = HomePageApp()
