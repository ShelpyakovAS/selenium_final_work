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
        assert self.is_correct_url(), "Login url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "fakemail"
        self.find_element_on_page(*LoginPageLocators.REGISTER_FORM_EMAIL).send_keys(email)
        self.find_element_on_page(*LoginPageLocators.REGISTER_FORM_PASS).send_keys(password)
        self.find_element_on_page(*LoginPageLocators.REGISTER_FORM_PASS2).send_keys(password)
        self.find_element_on_page(*LoginPageLocators.REGISTER_FORM_SUBMIT).click()

