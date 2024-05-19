from selene import browser


class ListItemsPage:

    def open_item_page_from_list(self):
        browser.all('.s-item.s-item__pl-on-bottom')[1].element('.s-item__link').click()

    def open_item_from_gallery(self):
        browser.all('.s-item.s-item__pl-on-bottom')[1].element('.s-item__link').click()

    def open_item_from_gallery_refurbished(self):
        browser.all('.s-item.s-item--large')[0].click()


list_items_pafe = ListItemsPage()
