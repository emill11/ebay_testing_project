from selene import browser, have, by
from ebay_testing_project.pages.web.home_page import home_page
from ebay_testing_project.pages.web.item_page import item_page
from ebay_testing_project.pages.web.list_items_page import list_items_pafe
from  time import sleep


def click_shop_by_category_button():
    browser.element('#gh-shop').click()

def open_electronics_section():
    browser.element('#gh-sbc-o').element(by.text('Electronics')).click()
def open_apple_section():
    browser.element('.dialog__cell').element(by.text('Apple')).click()
def open_watches_section():
    browser.element('.dialog__cell').element(by.text('Apple Watches')).click()
def open_item_from_list_from_section():
    browser.all('.s-item.s-item--large .s-item__image')[0].click()
def item_match_search_from_section():
    browser.element('div.d-breadcrumb__wrapper').should(have.text('Smart Watches'))
def test_navigation_panel_search():
    home_page.open_home_page()
    #нажать кнопку shop by category
    click_shop_by_category_button()

    #из выпадайки открыть категорию электроника
    open_electronics_section()

    #открыть категорию Apple
    open_apple_section()


    #открыть категорию Apple Watches
    open_watches_section()

    #открыть товар
    open_item_from_list_from_section()

    #новая вкладка
    #browser.driver.switch_to.window(browser.driver.window_handles[-1])
    item_page.switch_to_last_browser_tab()

    #товар соответствует
    item_match_search_from_section()




def test_by_categories_search():
    home_page.open_home_page()
    # из карусели "Explore Popular Categories" открыть раздел "Refurbished"
    home_page.open_refurbished_categories()
    # открыть раздел "Tools"
    home_page.open_tools_section()
    # открыть товар из списка
    list_items_pafe.open_item_from_gallery_refurbished()
    # проверить что в тексте есть слово Tools
    item_page.item_name_match_search_refurbished()
