from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
import allure


class CategoriesPage():

    def click_computers_tablets(self):
        with allure.step('Нажать Computers/Tablets & Networking'):
            browser.element(
                (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("Computers/Tablets & Networking")')).click()

    def click_3d_printers_supplies(self):
        with allure.step('Нажать 3D Printers & Supplies'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("3D Printers & Supplies")')).click()

    def click_3d_printers(self):
        with allure.step('Нажать 3D Printers'):
            browser.element((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("3D Printers")')).click()


categories_page = CategoriesPage()
