from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")

    def verify_cart_empty(self):
        expected_text = 'Your cart is empty'
        # actual_result = self.driver.find_element(*self.CART_EMPTY_TXT).text
        # assert expected_text == actual_text, f'Expected {expected_text}, got {actual_text}'
        # self.verify_text(expected_text,*self.CART_EMPTY_TXT)
        self.verify_text('Your cart is empty',*self.CART_EMPTY_TXT)