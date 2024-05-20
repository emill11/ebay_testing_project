from ebay_testing_project.pages.web.home_page import home_page
from ebay_testing_project.pages.web.item_page import item_page
from ebay_testing_project.pages.web.list_items_page import list_items_page


def test_recently_viewed_items():
    list_items_page.open_list_item()
    # открытие товара из списка
    list_items_page.open_item_from_gallery_refurbished()
    # скопировать название товара в переменную
    item_title = item_page.copy_item_name_to_variable()
    # открыть домашнюю страницу
    item_page.click_open_home_page_button()
    # сравнить название продукта с недано просмотренным
    home_page.match_recently_view_items(item_title)
