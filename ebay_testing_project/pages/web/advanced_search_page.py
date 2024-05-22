from selene import browser
import allure


class AdvancedSearchPage:

    def fill_keywords(self):
        with allure.step('Ввести в поле ввода текст'):
            browser.element('.floating-label').element('[data-testid="_nkw"]').type('headphones')

    def fill_located_in(self):
        with allure.step('Выбрать страну'):
            browser.element('[data-testid="s0-1-17-6[7]-5[@field[]]-_salic"]').click()
            browser.element('option[value="104"]').click()

    def click_search_advanced_button(self):
        with allure.step('Нажать кнопку Search'):
            browser.element('button.btn.btn--primary').click()


advanced_search_page = AdvancedSearchPage()
