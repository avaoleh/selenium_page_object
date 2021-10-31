from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    CART_BUTTON = (By.CSS_SELECTOR, ".basket-mini span a.btn.btn-default")
    CART_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")

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

