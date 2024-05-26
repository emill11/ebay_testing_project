from ebay_testing_project.pages.android_app.cart_page import cart_page
from ebay_testing_project.pages.android_app.home_page import home_page_app
from ebay_testing_project.pages.android_app.item_page import item_page
from ebay_testing_project.pages.android_app.list_items_page import list_items_page
from ebay_testing_project.utils.swipe_utils import swipe_up


def test_add_item_to_cart():
    # домашний экран
    home_page_app.open_app()
    home_page_app.click_search_field()
    home_page_app.fill_search_field()
    home_page_app.click_search_button_app()

    # Список товаров
    list_items_page.open_item()

    swipe_up(1)

    # товар
    item_page.click_add_to_cart_button()
    item_page.click_color_field()
    item_page.select_size()

    item_page.click_size_field()
    item_page.select_color()

    item_page.pop_up_click_go_to_cart()
    item_page.click_go_to_cart_button()

    # корзина
    cart_page.check_item_in_cart()
    cart_page.remove_item()
    cart_page.check_item_removed()
