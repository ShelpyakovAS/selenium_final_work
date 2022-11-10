from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_product_in_basket(self):
        add_button = self.find_element_on_page(*ProductPageLocators.BUTTON_ADD_PRODUCT_BASKET)
        add_button.click()
        self.solve_quiz_and_get_code()

    def check_product_in_basket(self):
        product_name = self.find_element_on_page(*ProductPageLocators.PRODUCT_NAME)
        product_price = self.find_element_on_page(*ProductPageLocators.PRODUCT_PRICE)
        add_product_name, any, add_product_price = self.find_elements_on_page(*ProductPageLocators.ADD_BASKET_ALERT_LIST)
        assert product_name.text == add_product_name.text and product_price.text == add_product_price.text, \
            'The name or price of the added product is not correct'



