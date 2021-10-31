from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # assert True
        assert "/login/" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # assert True
        assert self.is_element_present(*LoginPageLocators.LOGIN_FROM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # assert True
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


    def register_new_user(email, password):

        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_input.send_keys(email)

        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password_input1.send_keys(password)

        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password_input2.send_keys(password_test)

        submit_btn = self.browser.find_element(*BasePageLocators.REGISTRATION_SUBMIT)
        submit_btn.click()
