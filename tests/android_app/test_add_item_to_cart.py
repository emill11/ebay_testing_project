from ebay_testing_project.pages.android_app.cart_page import cart_page
from ebay_testing_project.pages.android_app.home_page import home_page_app
from ebay_testing_project.pages.android_app.item_page import item_page
from ebay_testing_project.pages.android_app.list_items_page import list_items_page
from ebay_testing_project.utils.swipe_utils import swipe_up
import allure
from allure_commons.types import Severity


@allure.epic('Add item to cart')
@allure.feature('Cart operations')
@allure.story('Add and Remove Item')
@allure.severity(Severity.CRITICAL)
@allure.tag('Android app')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_add_item_to_cart():
    # домашний экран
    home_page_app.open_app()
    home_page_app.click_search_field()

    # заполнить поле
    home_page_app.fill_search_field()

    home_page_app.click_search_button_app()

    # из списка открыть товар
    list_items_page.open_item()

    swipe_up(1)

    # нажать добавить в корзину
    item_page.click_add_to_cart_button()
    item_page.click_color_field()
    item_page.select_color()

    item_page.pop_up_click_go_to_cart()
    item_page.click_go_to_cart_button()

    # корзина
    cart_page.check_item_in_cart()
    cart_page.remove_item()
    cart_page.check_item_removed()
