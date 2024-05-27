from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, be


class WatchlistPage():
    def match_recently_view_items(self, product_title):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{product_title}")')).should(be.visible)

    def click_item_actions_button(self):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Item actions')).click()

    def remove_item_from_watchlist(self):
        browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))[4].click()

    def check_item_removed_from_watchlist(self):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("There\'s nothing here")')).should(
            be.visible)


watchlist_page = WatchlistPage()
