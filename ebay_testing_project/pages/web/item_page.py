from selene import browser, have, query


class ItemPage:

    def item_match_search_country(self):
        browser.all('.s-item.s-item__pl-on-bottom')[1].element('.s-item__location').should(have.text('from Japan'))

    def item_name_match_search(self):
        browser.element('div.d-breadcrumb__wrapper').should(have.text('Headphones'))

    def switch_to_last_browser_tab(self):
        browser.driver.switch_to.window(browser.driver.window_handles[-1])

    def item_name_match_search_refurbished(self):
        browser.element('div.d-breadcrumb__wrapper').should(have.text('Tools'))

    def click_add_to_cart_button(self):
        browser.element('#atcBtn_btn_1').click()

    def item_match_search_from_section(self):
        browser.element('div.d-breadcrumb__wrapper').should(have.text('Smart Watches'))

    def copy_item_name_to_variable(self):
        return browser.element('.x-item-title .ux-textspans--BOLD').get(query.text)

    def click_open_home_page_button(self):
        browser.element('#gh-la').click()


item_page = ItemPage()
