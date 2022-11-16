from .pages.main_page import MainPage
from .pages.locators import BasePageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # self.product = ProductFactory(title="Best book created by robot")
        # создаем по апи
        self.link = BasePageLocators.MAIN_PAGE_URL
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        # self.product.delete()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page(self, browser):
        link = BasePageLocators.MAIN_PAGE_URL
        page = MainPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = BasePageLocators.MAIN_PAGE_URL
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = BasePageLocators.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.basket_is_empty()