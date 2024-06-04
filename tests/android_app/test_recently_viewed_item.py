from ebay_testing_project.pages.android_app.home_page import home_page_app
from ebay_testing_project.pages.android_app.item_page import item_page
from ebay_testing_project.pages.android_app.list_items_page import list_items_page
from ebay_testing_project.pages.android_app.my_ebay_page import my_ebay_page
from ebay_testing_project.pages.android_app.watchlist_page import watchlist_page
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser
import allure
from allure_commons.types import Severity


@allure.epic('View items')
@allure.feature('View recently viewed items')
@allure.story('After viewing a product, it begins to appear in the recently viewed block')
@allure.severity(Severity.NORMAL)
@allure.tag('Android app')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_recently_viewed_item():
    home_page_app.open_app()
    home_page_app.click_search_field()
    home_page_app.fill_search_field()
    home_page_app.сlick_item_in_drop_down()
    list_items_page.open_item()
    item_title = item_page.copy_item_name_to_variable()
    my_ebay_page.my_ebay_button_click()
    my_ebay_page.click_recently_viewed()
    watchlist_page.match_recently_view_items(item_title)
