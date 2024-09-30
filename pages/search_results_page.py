from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class SearchResultsPage(Page):

    SEARCH_RESULTS_HEADER = By.XPATH, "//div[@data-test='resultsHeading']"
    ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")


    def verify_results(self, product):
        # actual_result = self.driver.find_element(*self.SEARCH_RESULTS_HEADER).text
        # assert product in actual_result, f'Expected {product}, got {actual_result}'
        self.verify_partial_text(product,*self.SEARCH_RESULTS_HEADER)

    def verify_results_url(self, product):
        self.verify_partial_url(product)

    def search_for_coffee(self):
        return self.find_element(*self.SEARCH_RESULTS_HEADER)


    def click_add_cart(self):
        # self.driver.execute_script("window.scrollTo(0, 490)")
        self.click(*self.ADD_TO_CART_BTN)  # always clicks on 1st Add to cart btn
        self.wait_for_element_to_appear(*self.SIDE_NAV_PRODUCT_NAME)

        sleep(5)

