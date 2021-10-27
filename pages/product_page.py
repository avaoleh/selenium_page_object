from .base_page import BasePage
from .locators import ProductPageLocators
import logging

LOGGER = logging.getLogger(__name__)


class ProductPage(BasePage):
    def go_to_basket_page(self):
        """
        Проверка наличие кнопки корзины и нажатие на нее
        """
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_solve_quiz_and_get_code(self):
        """
        Проверка, что клиент расчитал правильно формулу, для получения promo code
        """
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
        assert self.solve_quiz_and_get_code(), "Client can get the promo code"

    def should_be_correct_added_product(self):
        """
        Проверка, что выбранный продукт добавлен в корзину
        """
        self.should_be_correct_adding_product_title()
        # self.should_be_correct_adding_product_price()

    def should_be_correct_adding_product_title(self):
        """Проверка сообщения о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        """
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        print(product_name.text)
        print(item_name.text)
        assert product_name.text == item_name.text, "Product name in product page and product name in basket didn't match"

    def should_be_correct_adding_product_price(self):
        """
        Проверка сообщения со стоимостью корзины. Стоимость корзины совпадает с ценой товара
        """
        message_basket_total = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        print(product_price.text)
        print(message_basket_total.text)
        product_price_txt = "product_price: " + str(product_price.text)
        message_basket_total_txt = "message_basket_total: " + str(message_basket_total.text)
        LOGGER.info(product_price_txt)
        LOGGER.info(message_basket_total_txt)
        assert product_price.text == message_basket_total.text, "Product price in product page and product price in basket didn't match"

