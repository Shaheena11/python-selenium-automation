from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")
    SIGN_IN_BTN2 = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def search_product(self, item):
        self.input_text(text=item, *self.SEARCH_FIELD,)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load

    def click_cart(self):
        self.wait_to_be_clickable_click(*self.CART_BTN)


    def click_sign_in(self):
        self.click(*self.SIGN_IN_BTN)
        sleep(2)

    def right_side_click_sign_in(self):
        self.click(*self.SIGN_IN_BTN2)
        sleep(5)

