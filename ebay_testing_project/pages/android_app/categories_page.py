from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


class CategoriesPage():

    def click_computers_tablets(self):
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("Computers/Tablets & Networking")')).click()

    def click_3d_printers_supplies(self):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("3D Printers & Supplies")')).click()

    def click_3d_printers(self):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("3D Printers")')).click()


categories_page = CategoriesPage()
