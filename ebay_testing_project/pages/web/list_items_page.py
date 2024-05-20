from selene import browser, by


class ListItemsPage:

    def open_item_page_from_list(self):
        browser.all('.s-item.s-item__pl-on-bottom')[1].element('.s-item__link').click()

    def open_item_from_gallery_refurbished(self):
        browser.all('.s-item.s-item--large')[1].click()

    def open_list_item(self):
        browser.open('e/row/toolsrefurbishedrow')

    def open_apple_section(self):
        browser.element('.dialog__cell').element(by.text('Apple')).click()

    def open_watches_section(self):
        browser.element('.dialog__cell').element(by.text('Apple Watches')).click()

    def open_item_from_watches_section(self):
        browser.all('.s-item.s-item--large .s-item__image')[0].click()


list_items_page = ListItemsPage()
