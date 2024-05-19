from selene import browser


class AdvancedSearchPage:
    def fill_keywords(self):
        browser.element('.floating-label').element('[data-testid="_nkw"]').type('headphones')

    def fill_located_in(self):
        browser.element('[data-testid="s0-1-17-6[7]-[4]-LH_LocatedIn"]').click()
        browser.element('[data-testid="s0-1-17-6[7]-5[@field[]]-_salic"]').click()
        browser.element('option[value="104"]').click()

    def click_search_advanced_button(self):
        browser.element('button.btn.btn--primary').click()


advanced_search_page = AdvancedSearchPage()
