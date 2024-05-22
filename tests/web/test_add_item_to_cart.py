from ebay_testing_project.pages.web.cart_page import cart_page
from ebay_testing_project.pages.web.item_page import item_page
from ebay_testing_project.pages.web.list_items_page import list_items_page


def test_add_item_to_cart():
    list_items_page.open_list_item()
    # открытие товара из списка
    list_items_page.open_item_from_gallery_refurbished()  # browser.all('.s-item.s-item--large')[0].click()

    # добавление товара в корзину и переход в корзину
    item_page.click_add_to_cart_button()



    # проверка что в корзину добавлена одна штука товара
    cart_page.item_added_to_cart_check()

    # удаление товара
    cart_page.item_remove_from_cart()

    # проверка что товар удален
    cart_page.cart_is_empty_check()
