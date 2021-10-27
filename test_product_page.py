import pytest
import time
from selenium import webdriver
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_basket_page()        # нажать на кнопку "add to basket"
    page.should_solve_quiz_and_get_code()   # решаем quiz
    # time.sleep(5)
    page.should_be_correct_added_product()  # проверяем корректность цены и названия продукта
