from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


def test_guest_can_go_to_login_page(browser):
    link = LoginPageLocators.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()


def test_register_form_in_login_page(browser):
    link = LoginPageLocators.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.is_element_present(*LoginPageLocators.REGISTER_FORM)


def test_login_form_in_login_page(browser):
    link = LoginPageLocators.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.is_element_present(*LoginPageLocators.LOGIN_FORM)
