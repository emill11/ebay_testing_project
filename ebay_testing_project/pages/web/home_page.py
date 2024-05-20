from selene import browser, by, have
import allure


class HomePage:

    def open_home_page(self):
        with allure.step('Открыть домашнюю страницу'):
            browser.open('/')

    def fill_in_search(self):
        with allure.step('Ввести текст в поле поиска'):
            browser.element('.gh-tb.ui-autocomplete-input').type('Headphones')

    def click_search_button(self):
        with allure.step('Нажать кнопку Search'):
            browser.element('#gh-btn').click()

    def click_advanced_button(self):
        with allure.step('Нажать кнопку Advanced'):
            browser.element('#gh-as-td').click()

    def open_refurbished_categories(self):
        with allure.step('В блоке "Explore Popular Categories" нажать на иконку Refurbished'):
            browser.element('[data-m-id="4776"]').all('.vl-carousel__item')[3].click()

    def open_tools_section(self):
        with allure.step('Нажать на изображение Tools'):
            browser.all('.carousel__snap-point')[7].click()

    def click_shop_by_category_button(self):
        with allure.step('Нажать кнопку Shop by category'):
            browser.element('#gh-shop').click()

    def open_electronics_section(self):
        with allure.step('В выпадающем списке нажать на пункт Electronics'):
            browser.element('#gh-sbc-o').element(by.text('Electronics')).click()

    def match_recently_view_items(self, product_title):
        with allure.step('В блоке "Your Recently Viewed Items" отображается просмотренный товар'):
            browser.element('.vlp-merch-content-wrap').should(have.text(product_title))


home_page = HomePage()
