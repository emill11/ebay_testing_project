import allure
from selene import browser, by, have


class ListItemsPage:

    def open_item_page_from_list(self):
        with allure.step('Открыть товар из списка'):
            browser.all('.s-item.s-item__pl-on-bottom')[1].element('.s-item__link').click()

    def open_item_from_gallery_refurbished(self):
        with allure.step('Открыть товар из галереи'):
            browser.all('.s-item.s-item--large')[1].click()

    def open_list_item(self):
        with allure.step('Открыть список товаров через url'):
            browser.open('e/row/toolsrefurbishedrow')

    def open_apple_section(self):
        with allure.step('В боковом меню выбрать пункт Apple'):
            browser.element('.dialog__cell').element(by.text('Apple')).click()

    def open_watches_section(self):
        with allure.step('В боковом меню выбрать пункт Watches'):
            browser.element('.dialog__cell').element(by.text('Apple Watches')).click()

    def open_item_from_watches_section(self):
        with allure.step('Нажать на товар из списка'):
            browser.all('.s-item.s-item--large .s-item__image')[0].click()

    def item_match_search_country(self):
        with allure.step('Проверить что товар из выбранной страны'):
            browser.all('.s-item.s-item__pl-on-bottom')[1].element('.s-item__location').should(have.text('from Japan'))


list_items_page = ListItemsPage()
