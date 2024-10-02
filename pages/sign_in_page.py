from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Sign_In(Page):
    ACTUAL_RESULT = (By.XPATH, "//span[text()='Sign into your Target account']")
    T_AND_C_BTN = (By.CSS_SELECTOR, 'a[aria-label*="terms & conditions"]')

    def open_sign_in(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')
        sleep(5)

    def verify_sign_in_from_open(self):
        self.verify_text('Sign into your Target account',*self.ACTUAL_RESULT)

    def click_t_and_c_link(self):
        self.click(*self.T_AND_C_BTN)
        sleep(3)

    def verify_terms_and_conditions_page(self):
        self.verify_url('https://www.target.com/c/terms-conditions/-/N-4sr7l')

