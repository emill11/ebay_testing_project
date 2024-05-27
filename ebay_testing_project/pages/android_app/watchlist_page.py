from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be
import allure


class WatchlistPage():
    def match_recently_view_items(self, product_title):
        with allure.step('Название продукта соответствует'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{product_title}")')).should(
                be.visible)

    def click_item_actions_button(self):
        with allure.step('Нажать на иконку многоточие'):
            browser.element((AppiumBy.ACCESSIBILITY_ID, 'Item actions')).click()

    def remove_item_from_watchlist(self):
        with allure.step('Удалить продукт'):
            browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[4].click()

    def check_item_removed_from_watchlist(self):
        with allure.step('Проверить что продукт удален'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("There\'s nothing here")')).should(
                be.visible)


watchlist_page = WatchlistPage()
