from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FROM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
     BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

     PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
     CART_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

     PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main > h1')
     ITEM_NAME = (By.CSS_SELECTOR, 'div.page_inner > ul.breadcrumb > li.active')

     SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

