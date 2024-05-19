from selene import browser, have


class ItemPage:

    def item_match_main_search(self):
        browser.element('div.d-breadcrumb__wrapper').should(have.text('Headphones'))

    def item_match_search_country(self):
        browser.all('.s-item.s-item__pl-on-bottom')[1].element('.s-item__location').should(have.text('from Japan'))

    def item_name_match_search(self):
        browser.element('div.d-breadcrumb__wrapper').should(have.text('Sunglasses'))

    def switch_to_last_browser_tab(self):
        browser.driver.switch_to.window(browser.driver.window_handles[-1])

    def item_name_match_search_refurbished(self):
        browser.element('div.d-breadcrumb__wrapper').should(have.text('Tools'))


item_page = ItemPage()
