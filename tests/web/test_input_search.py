from ebay_testing_project.pages.web.advanced_search_page import advanced_search_page
from ebay_testing_project.pages.web.list_items_page import list_items_page
from ebay_testing_project.pages.web.home_page import home_page
from ebay_testing_project.pages.web.item_page import item_page
import allure
from allure_commons.types import Severity


@allure.epic('Search Product')
@allure.feature('Main Search')
@allure.story('Search item by name')
@allure.severity(Severity.CRITICAL)
@allure.tag('WEB')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_main_search():
    home_page.open_home_page()
    home_page.fill_in_search()
    home_page.click_search_button()
    list_items_page.open_item_page_from_list()
    item_page.switch_to_last_browser_tab()
    item_page.item_name_match_search()


@allure.epic('Search Product')
@allure.feature('Advanced Search')
@allure.story('Search for a product by name with a filter by country')
@allure.severity(Severity.NORMAL)
@allure.tag('WEB')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_advanced_search():
    home_page.open_home_page()
    home_page.click_advanced_button()
    advanced_search_page.fill_keywords()
    advanced_search_page.fill_located_in()
    advanced_search_page.click_search_advanced_button()
    list_items_page.item_match_search_country()
    list_items_page.open_item_page_from_list()
    item_page.switch_to_last_browser_tab()
    item_page.item_name_match_search()
