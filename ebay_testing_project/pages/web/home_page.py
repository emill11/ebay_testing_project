from selene import browser


class HomePage:
    def open_home_page(self):
        browser.open('/')

    def fill_in_search(self):
        browser.element('.gh-tb.ui-autocomplete-input').type('Sunglasses')

    def click_search_button(self):
        browser.element('#gh-btn').click()

    def click_advanced_button(self):
        browser.element('#gh-as-td').click()

    def open_refurbished_categories(self):
        browser.element('[data-m-id="4776"]').all('.vl-carousel__item')[3].click()

    def open_tools_section(self):
        browser.all('.carousel__snap-point')[7].click()


home_page = HomePage()
