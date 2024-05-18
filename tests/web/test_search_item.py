from selene import browser, have, by
from ebay_testing_project.pages.web.home_page import home_page


def fill_in_search():
    browser.element('.gh-tb.ui-autocomplete-input').type('Sunglasses')


def click_search_button():
    browser.element('#gh-btn').click()


def open_item_page():
    browser.all('.s-item.s-item__pl-on-bottom')[1].click()
    browser.driver.switch_to.window(browser.driver.window_handles[-1])


def element_matches_search():
    browser.element('div.d-breadcrumb__wrapper').should(have.text('Sunglasses'))


def test_main_search():
    home_page.open_home_page()
    # на главной странице, ввод в поле поиска текст и клик
    fill_in_search()
    click_search_button()
    #
    open_item_page()
    element_matches_search()


'''ниже расширенный поиск по стране'''


def click_advanced_button():
    browser.element('#gh-as-td').click()


def fill_keywords():
    browser.element('.floating-label').element('[data-testid="_nkw"]').type('headphones')


def fill_located_in():
    browser.element('[data-testid="s0-1-17-6[7]-[4]-LH_LocatedIn"]').click()
    browser.element('[data-testid="s0-1-17-6[7]-5[@field[]]-_salic"]').click()
    browser.element('option[value="104"]').click()


def click_search_advanced_button():
    browser.element('button.btn.btn--primary').click()


def item_found_in_advanced_search():
    browser.all('.s-item.s-item__pl-on-bottom')[1].element('.s-item__location').should(have.text('from Japan'))


def test_advanced_search():
    home_page.open_home_page()
    # нажать на кнопку перехода к расширенному поиску
    click_advanced_button()
    # ввести в поле ввода текст
    fill_keywords()
    # нажать на радиокнопку откуда
    # нажать на поле выбора страны
    # в выпадайке выбрать Japan
    fill_located_in()
    # нажать далее
    click_search_advanced_button()
    # проверить откуда товар
    item_found_in_advanced_search()
    # открыть товар
    browser.all('.s-item.s-item__pl-on-bottom')[1].element('.s-item__link').click()
    # проверить название товара
    browser.driver.switch_to.window(browser.driver.window_handles[-1])
    browser.element('div.d-breadcrumb__wrapper').should(have.text('Headphones'))


'''ниже поиск и открытие через навигационную панель'''


def test_navigation_panel_search():
    home_page.open_home_page()
    browser.element('#gh-shop').click()
    browser.element('#gh-sbc-o').element(by.text('Electronics')).click()
    browser.element('.dialog__cell').element(by.text('Apple')).click()
    browser.element('.dialog__cell').element(by.text('Apple Watches')).click()
    browser.all('.s-item.s-item--large .s-item__image')[0].click()
    browser.driver.switch_to.window(browser.driver.window_handles[-1])
    browser.element('div.d-breadcrumb__wrapper').should(have.text('Smart Watches'))
