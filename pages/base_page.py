from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_correct_url(self):
        if self.url == self.browser.current_url:
            return True
        return False

    def find_element_on_page(self, how, what):
        return self.browser.find_element(how, what)

    def find_elements_on_page(self, how, what):
        return self.browser.find_elements(how, what)
