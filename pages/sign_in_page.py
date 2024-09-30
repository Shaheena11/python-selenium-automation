from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Sign_In(Page):
    ACTUAL_RESULT = (By.XPATH, "//span[text()='Sign into your Target account']")

    def verify_sign_in_from_open(self):
        self.verify_text('Sign into your Target account',*self.ACTUAL_RESULT)
