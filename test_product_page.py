from .pages.product_page import ProductPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.check_product_in_basket()

@pytest.mark.parametrize('link_i', [i for i in range(10)])
def test_guest_can_add_product_to_basket_promo(browser, link_i):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer' + str(link_i)
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.check_product_in_basket()