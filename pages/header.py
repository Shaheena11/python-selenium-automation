from selenium.webdriver.common.by import By
from time import sleep
from features.steps.hw5_1_wait import SEARCH_INPUT
from pages.base_page import Page



class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")


    def search_products(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load