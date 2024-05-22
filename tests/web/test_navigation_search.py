from ebay_testing_project.pages.web.home_page import home_page
from ebay_testing_project.pages.web.item_page import item_page
from ebay_testing_project.pages.web.list_items_page import list_items_page


def test_navigation_panel_search():
    home_page.open_home_page()
    # нажать кнопку shop by category
    home_page.click_shop_by_category_button()

    # из выпадайки открыть категорию электроника
    home_page.open_electronics_section()

    # открыть категорию Apple
    list_items_page.open_apple_section()

    # открыть категорию Apple Watches
    list_items_page.open_watches_section()

    # открыть товар
    list_items_page.open_item_from_watches_section()

    # новая вкладка
    # browser.driver.switch_to.window(browser.driver.window_handles[-1])
    item_page.switch_to_last_browser_tab()

    # товар соответствует
    item_page.item_match_search_from_section()


def test_by_categories_search():
    home_page.open_home_page()
    #открыть jordan jumpman
    home_page.open_refurbished_categories()

    # # открыть раздел "Tools"
    # home_page.open_tools_section()
    #в попапе нажать открыть корзину
    item_page.click_open_cart_button()

    # открыть товар из списка
    list_items_page.open_item_from_gallery_refurbished()
    # проверить что в тексте есть слово Tools
    item_page.item_name_match_search_refurbished()
