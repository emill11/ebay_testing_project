import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class ItemPage():

    def click_add_to_cart_button(self):
        with allure.step('Нажать добавить в корзину'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/cta_button_plus')).click()

    def click_color_field(self):
        with allure.step('Нажать на поле выборва цвета'):
            browser.all((AppiumBy.ID, 'com.ebay.mobile:id/spinner_selection_option'))[0].click()

    def select_color(self):
        with allure.step('Выбрать цвет'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/image')).click()

    def click_size_field(self):
        with allure.step('Нажать на поле выбора размера'):
            browser.all((AppiumBy.ID, 'com.ebay.mobile:id/spinner_selection_option'))[1].click()

    def select_size(self):
        with allure.step('Выбрать размер'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/text')).click()

    def pop_up_click_add_to_cart_button(self):
        with allure.step('Нажать кнопку Add to cart'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/buy_bar_button')).click()

    def click_go_to_cart_button(self):
        with allure.step('нажать кнопку Go to cart'):
            browser.element((AppiumBy.ID, 'com.ebay.mobile:id/call_to_action_button')).click()


item_page = ItemPage()
