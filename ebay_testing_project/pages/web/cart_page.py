from selene import browser, have
import allure


class CartPage:

    def item_added_to_cart_check(self):
        with allure.step('Проверить, что в корзину добавлен продукт'):
            browser.all('[data-test-id="qty-dropdown"]')[0].element('option[value="1"]').should(
                have.attribute('selected'))

    def item_remove_from_cart(self):
        with allure.step('Удалить продукт из корзины'):
            browser.element('[data-test-id="cart-remove-item"]').click()

    def cart_is_empty_check(self):
        with allure.step('Проверить что корзина пуста'):
            browser.element('#page-alerts').element('span').should(have.text('was removed from your cart.'))


cart_page = CartPage()
