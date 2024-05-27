import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, query, be


class ItemPage():

    def click_add_to_cart_button(self):
        with allure.step('Нажать добавить в корзину'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/cta_button_plus')).click()

    def click_color_field(self):
        with allure.step('Нажать на поле выборва цвета'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/spinner_selection_option')).click()

    def select_color(self):
        with allure.step('Выбрать цвет'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/image')).click()

    def pop_up_click_go_to_cart(self):
        with allure.step('Нажать кнопку Add to cart'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/buy_bar_button')).click()

    def click_go_to_cart_button(self):
        with allure.step('нажать кнопку Go to cart'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/call_to_action_button')).click()

    def click_add_to_watchlist(self):
        with allure.step('нажать кнопку add to watchlist'):
            browser.all((AppiumBy.ID, 'com.ebay.mobile:id/cta_button_plus'))[1].click()

    def copy_item_name_to_variable(self):
        with allure.step('Скопировать название продукта в переменную'):
            return browser.element(
                (AppiumBy.XPATH, '//androidx.compose.ui.platform.ComposeView//android.widget.TextView')).get(
                query.text).strip()

    def match_brand(self):
        with allure.step('Продукт соответствует поиску'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("ANYCUBIC")')).should(be.visible)


item_page = ItemPage()
