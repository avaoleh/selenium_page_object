from .base_page import BasePage
from .locators import BasePageLocators

import logging

LOGGER = logging.getLogger(__name__)

class BasketPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_element_present(*BasePageLocators.CART_EMPTY), "Cart is not empty"

    def should_not_be_empty_cart(self):
        assert self.is_not_element_present(*BasePageLocators.CART_EMPTY), "Cart is not empty, but should not be"
