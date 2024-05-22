from ebay_testing_project.pages.web.cart_page import cart_page
from ebay_testing_project.pages.web.item_page import item_page
from ebay_testing_project.pages.web.list_items_page import list_items_page
import allure
from allure_commons.types import Severity


@allure.epic('Add item to cart')
@allure.feature('Cart operations')
@allure.story('Add and Remove Item')
@allure.severity(Severity.CRITICAL)
@allure.tag('WEB')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_add_item_to_cart():
    list_items_page.open_list_item()
    list_items_page.open_item_from_gallery_refurbished()
    item_page.click_add_to_cart_button()
    cart_page.item_added_to_cart_check()
    cart_page.item_remove_from_cart()
    cart_page.cart_is_empty_check()
