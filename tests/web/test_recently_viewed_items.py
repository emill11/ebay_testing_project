from ebay_testing_project.pages.web.home_page import home_page
from ebay_testing_project.pages.web.item_page import item_page
from ebay_testing_project.pages.web.list_items_page import list_items_page
import allure
from allure_commons.types import Severity


@allure.epic('View items')
@allure.feature('View recently viewed items')
@allure.story('After viewing a product, it begins to appear in the recently viewed block')
@allure.severity(Severity.NORMAL)
@allure.tag('WEB')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_recently_viewed_items():
    list_items_page.open_list_item()
    list_items_page.open_item_from_gallery_refurbished()
    item_title = item_page.copy_item_name_to_variable()
    item_page.click_open_home_page_button()
    home_page.match_recently_view_items(item_title)
