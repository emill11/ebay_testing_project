from ebay_testing_project.pages.android_app.home_page import home_page_app
from ebay_testing_project.pages.android_app.item_page import item_page
from ebay_testing_project.pages.android_app.list_items_page import list_items_page
from ebay_testing_project.pages.android_app.my_ebay_page import my_ebay_page
from ebay_testing_project.pages.android_app.watchlist_page import watchlist_page
from ebay_testing_project.utils.swipe_utils import swipe_up, swipe_down
import allure
from allure_commons.types import Severity


@allure.epic('Add item to watchlist')
@allure.feature('watchlist operations')
@allure.story('Add and Remove Item')
@allure.severity(Severity.CRITICAL)
@allure.tag('Android app')
@allure.label('owner', 'Emil')
@allure.label('layer', 'UI')
def test_add_item_to_watchlist():
    home_page_app.open_app()
    home_page_app.click_search_field()
    home_page_app.fill_search_field()
    home_page_app.сlick_item_in_drop_down()
    list_items_page.open_item()
    item_title = item_page.copy_item_name_to_variable()
    swipe_up(1)
    item_page.click_add_to_watchlist()
    item_page.click_color_field()
    item_page.select_color()
    item_page.pop_up_click_go_to_cart()
    swipe_down(2)
    my_ebay_page.my_ebay_button_click()
    my_ebay_page.watchlist_button_click()
    watchlist_page.match_recently_view_items(item_title)
    watchlist_page.click_item_actions_button()
    watchlist_page.remove_item_from_watchlist()
    watchlist_page.check_item_removed_from_watchlist()
