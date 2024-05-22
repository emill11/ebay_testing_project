from selene import browser, have, query
import allure


class ItemPage:

    def item_name_match_search(self):
        with allure.step('Проверить что товар соответствует поиску'):
            browser.element('div.d-breadcrumb__wrapper').should(have.text('Headphones').or_(have.text('Headset')))

    def switch_to_last_browser_tab(self):
        with allure.step('Переключение драйвера на последнюю вкладку браузера'):
            browser.driver.switch_to.window(browser.driver.window_handles[-1])

    def item_name_match_search_refurbished(self):
        with allure.step('Проверить что товар соответствует поиску'):
            browser.element('[data-testid="d-breadcrumb"]').should(have.text('Power Tools'))

    def click_add_to_cart_button(self):
        with allure.step('Нажать кнопку Add to cart'):
            browser.element('#atcBtn_btn_1').click()

    def item_match_search_from_section(self):
        with allure.step('Проверить что товар соответствует поиску'):
            browser.element('div.d-breadcrumb__wrapper').should(have.text('Smart Watches'))

    def copy_item_name_to_variable(self):
        with allure.step('Скопировать название товара в переменную'):
            return browser.element('.x-item-title .ux-textspans--BOLD').get(query.text)

    def click_open_home_page_button(self):
        with allure.step('Нажать на логотип'):
            browser.element('#gh-la').click()


item_page = ItemPage()
