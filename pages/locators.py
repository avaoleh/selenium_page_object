from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FROM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
     BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

     PRODUCT_PRICE = (By.CSS_SELECTOR, ".basket-mini :nth-child(1) ")
     CART_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

     PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
     ITEM_NAME = (By.CSS_SELECTOR, 'div.page_inner > ul.breadcrumb > li.active')

