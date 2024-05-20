from selene import browser, by, have


class HomePage:
    def open_home_page(self):
        browser.open('/')

    def fill_in_search(self):
        browser.element('.gh-tb.ui-autocomplete-input').type('Headphones')

    def click_search_button(self):
        browser.element('#gh-btn').click()

    def click_advanced_button(self):
        browser.element('#gh-as-td').click()

    def open_refurbished_categories(self):
        browser.element('[data-m-id="4776"]').all('.vl-carousel__item')[3].click()

    def open_tools_section(self):
        browser.all('.carousel__snap-point')[7].click()

    def click_shop_by_category_button(self):
        browser.element('#gh-shop').click()

    def open_electronics_section(self):
        browser.element('#gh-sbc-o').element(by.text('Electronics')).click()

    def match_recently_view_items(self, product_title):
        browser.element('.vlp-merch-content-wrap').should(
            have.text(product_title))


home_page = HomePage()
