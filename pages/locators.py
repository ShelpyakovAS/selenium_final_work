from selenium.webdriver.common.by import By
import re


class BasePageLocators:
    MAIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, f'a[href="/en-gb/basket/"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_PAGE_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_FORM_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_FORM_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    BUTTON_ADD_PRODUCT_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADD_BASKET_ALERT_LIST = (By.CSS_SELECTOR, '.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div')


class BasketPageLocators:
    BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
