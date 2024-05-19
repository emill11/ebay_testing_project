from selene import browser, have, have, query
from time import sleep
from ebay_testing_project.pages.web.home_page import home_page


def test_recently_viewed_items():
    browser.open('e/row/toolsrefurbishedrow')

    # открытие товара из списка
    browser.all('.s-item.s-item--large')[0].click()
    # скопировать название товара в переменную
    product_title = browser.element('.x-item-title .ux-textspans--BOLD').get(query.text)
    # открыть домашнюю страницу
    browser.element('#gh-la').click()

    # сравнить название продукта с недано просмотренным
    browser.element('.vlp-merch-content-wrap').should(
        have.text(product_title))
