from selene import browser, have
from time import sleep
from ebay_testing_project.pages.web.home_page import home_page


def test_add_product_to_cart():
    home_page.open_home_page()

    # def test_select_product_category():
    # переход по цепочке категорий товара(главный экран>экран товары для дома>экран инструменты)
    browser.element('[data-m-id="4776"]').all('.vl-carousel__item')[3].click()
    browser.all('.carousel__snap-point')[7].click()

    # def test_open_product_from_list():  # открытие товара из списка
    browser.all('.s-item.s-item--large')[0].click()

    # def test_add_product_to_cart():
    # добавление товара в корзину и переход в корзину
    browser.element('#atcBtn_btn_1').click()

    # def test_check_product_added_to_cart():
    # проверка что в корзину добавлена одна штука товара
    browser.all('[data-test-id="qty-dropdown"]')[0].element('option[value="1"]').should(
        have.attribute('selected'))

    # def test_remove_product_from_cart():
    # удаление товара
    browser.element('[data-test-id="cart-remove-item"]').click()

    # def test_check_product_removed_from_cart():
    # проверка что товар удален
    browser.element('#page-alerts').element('span').should(have.text('was removed from your cart.'))
    sleep(5)
