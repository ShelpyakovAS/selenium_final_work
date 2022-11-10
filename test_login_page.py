from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


def test_can_go_to_login_page(browser):
    link = LoginPageLocators.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()


def test_register_form_in_login_page(browser):
    link = LoginPageLocators.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


def test_login_form_in_login_page(browser):
    link = LoginPageLocators.LOGIN_PAGE_URL
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
