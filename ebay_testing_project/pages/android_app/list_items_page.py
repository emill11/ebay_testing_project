import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class ListItemsPage():

    def open_item(self):
        with allure.step('Нажать на первый товар в списке'):
            browser.all((AppiumBy.ID, 'com.ebay.mobile:id/cell_collection_item'))[0].click()


list_items_page = ListItemsPage()
