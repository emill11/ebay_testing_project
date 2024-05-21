from ebay_testing_project.pages.web.advanced_search_page import advanced_search_page
from ebay_testing_project.pages.web.list_items_page import list_items_page
from ebay_testing_project.pages.web.home_page import home_page
from ebay_testing_project.pages.web.item_page import item_page


def test_main_search():
    home_page.open_home_page()
    # на главной странице, ввод в поле поиска текст
    home_page.fill_in_search()
    # на главной стр клик на кнопку поиска
    home_page.click_search_button()
    # открытие товара из результата главного поиска
    list_items_page.open_item_page_from_list()
    item_page.switch_to_last_browser_tab()
    # проверка что название товара соответствует поиску
    item_page.item_name_match_search()


def test_advanced_search():
    home_page.open_home_page()
    # нажать на кнопку перехода к расширенному поиску
    home_page.click_advanced_button()
    # ввести в поле ввода текст
    advanced_search_page.fill_keywords()
    # нажать на радиокнопку откуда
    # нажать на поле выбора страны
    # в выпадайке выбрать Japan
    advanced_search_page.fill_located_in()
    # нажать далее
    advanced_search_page.click_search_advanced_button()

    list_items_page.switch_to_list_view()

    # проверить откуда товар
    list_items_page.item_match_search_country()
    # открыть товар
    list_items_page.open_item_page_from_list()
    # проверить название товара
    item_page.switch_to_last_browser_tab()
    item_page.item_name_match_search()
