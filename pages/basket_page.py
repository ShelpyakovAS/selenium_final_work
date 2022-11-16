from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty(self):
        assert 'Your basket is empty' in self.find_element_on_page(*BasketPageLocators.BASKET_EMPTY).text, \
            "Basket is not empty"
