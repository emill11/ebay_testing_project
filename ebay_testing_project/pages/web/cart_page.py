from selene import browser, have


class CartPage:

    def item_added_to_cart_check(self):
        browser.all('[data-test-id="qty-dropdown"]')[0].element('option[value="1"]').should(have.attribute('selected'))

    def item_remove_from_cart(self):
        browser.element('[data-test-id="cart-remove-item"]').click()

    def cart_is_empty_check(self):
        browser.element('#page-alerts').element('span').should(have.text('was removed from your cart.'))


cart_page = CartPage()
