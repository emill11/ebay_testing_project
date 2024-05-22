from ebay_testing_project.pages.web.home_page import home_page
from ebay_testing_project.pages.web.item_page import item_page
from ebay_testing_project.pages.web.list_items_page import list_items_page
import allure
from allure_commons.types import Severity


@allure.epic('Search Product')
@allure.feature('Navigation Bar Search')
@allure.story('Search for a product via the navigation bar')
@allure.severity(Severity.CRITICAL)
@allure.tag('WEB')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_navigation_panel_search():
    home_page.open_home_page()
    home_page.click_shop_by_category_button()
    home_page.open_electronics_section()
    list_items_page.open_apple_section()
    list_items_page.open_watches_section()
    list_items_page.open_item_from_watches_section()
    item_page.switch_to_last_browser_tab()
    item_page.item_match_search_from_section()


@allure.epic('Search Product')
@allure.feature('Recommended Categories Search')
@allure.story('Search for products through recommended categories')
@allure.severity(Severity.CRITICAL)
@allure.tag('WEB')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_by_categories_search():
    home_page.open_home_page()
    home_page.open_refurbished_categories()
    home_page.open_tools_section()
    list_items_page.open_item_from_gallery_refurbished()
    item_page.item_name_match_search_refurbished()
