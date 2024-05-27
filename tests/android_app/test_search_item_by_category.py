from ebay_testing_project.pages.android_app.categories_page import categories_page
from ebay_testing_project.pages.android_app.home_page import home_page_app
from ebay_testing_project.pages.android_app.item_page import item_page
from ebay_testing_project.pages.android_app.list_items_page import list_items_page
from ebay_testing_project.utils import swipe_utils
import allure
from allure_commons.types import Severity


@allure.epic('Search Product')
@allure.feature('Categories search')
@allure.story('Search for products through categories')
@allure.severity(Severity.CRITICAL)
@allure.tag('Android app')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_search_item_by_category():
    home_page_app.open_app()
    home_page_app.click_categories()
    swipe_utils.swipe_up(2)
    categories_page.click_computers_tablets()
    categories_page.click_3d_printers_supplies()
    categories_page.click_3d_printers()
    list_items_page.click_brand()
    list_items_page.open_item()
    swipe_utils.swipe_up(2)
    item_page.match_brand()
