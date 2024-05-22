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

    def switch_to_list_view(self):
        with allure.step('Установить расположение товаров в виде списка'):
            # browser.element('.icon.icon--grid-view-16').click()
            # browser.element('#nid-eg0-0 .btn__cell').all('.fake-menu-button__item')[0].click()

            # browser.element('[aria-label="Listing options selector. Gallery View selected."]').click()
            #browser.element('#nid-eg0-0 .fake-menu-button__button').click()

            browser.element('.srp-controls__control.srp-view-options').click()
            browser.element('.srp-controls__control.srp-view-options').all('.fake-menu-button__item')[0].click()


list_items_page = ListItemsPage()
