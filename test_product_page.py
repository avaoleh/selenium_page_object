import pytest
import time
from selenium import webdriver
from .pages.product_page import ProductPage

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]

@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_cart(browser, product: str) -> None:
    link = product
    #3) link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #2) link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #1) link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_basket_page()        # нажать на кнопку "add to basket"
    page.should_solve_quiz_and_get_code()   # решаем quiz
    # time.sleep(5)
    # page.should_be_correct_added_product()  # проверяем корректность цены и названия продукта
