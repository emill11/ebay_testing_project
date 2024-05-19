from selene import browser, have
from time import sleep
from ebay_testing_project.pages.web.advanced_search_page import advanced_search_page


def open_list_item():
    browser.open('e/row/toolsrefurbishedrow')


def test_add_product_to_cart():
    open_list_item()
    # открытие товара из списка
    browser.all('.s-item.s-item--large')[0].click()
    # добавление товара в корзину и переход в корзину
    browser.element('#atcBtn_btn_1').click()

    # проверка что в корзину добавлена одна штука товара
    browser.all('[data-test-id="qty-dropdown"]')[0].element('option[value="1"]').should(
        have.attribute('selected'))

    # удаление товара
    browser.element('[data-test-id="cart-remove-item"]').click()

    # проверка что товар удален
    browser.element('#page-alerts').element('span').should(have.text('was removed from your cart.'))
    sleep(5)
