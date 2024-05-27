import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class CartPage():
    def check_item_in_cart(self):
        with allure.step('Проверить наличие продукта в карзине'):
            browser.element((AppiumBy.CLASS_NAME, 'android.widget.EditText')).should(have.text('1'))

    def remove_item(self):
        with allure.step('Удалить продукт'):
            browser.element((AppiumBy.CLASS_NAME, 'android.widget.Button')).click()

    def check_item_removed(self):
        with allure.step('Проверить что продукт удален'):
            browser.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(
                have.text("You don't have any items in your cart. Let's get shopping!"))


cart_page = CartPage()
