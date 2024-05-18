from selene import browser, have, have, query
from time import sleep
from ebay_testing_project.pages.web.home_page import home_page


def test_recently_viewed_items():
    browser.open('/')
    # добавить предварительные шаги
    product_title = browser.element('.x-item-title .ux-textspans--BOLD').get(query.text)
    browser.element('#gh-la').click()
    sleep(5)
    browser.element('.vlp-merch-content-wrap').should(
        have.text(product_title))
    sleep(5)
