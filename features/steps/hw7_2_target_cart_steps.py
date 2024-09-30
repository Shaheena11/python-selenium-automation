from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from features.steps.hw6_2_search_result_steps import ADD_TO_CART_BTN

ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

@when('Search {item}')
def search_product(context, item):
    context.app.header.search_product(item)
    sleep(15)

@then('Click on Add to Cart Button')
def click_add_cart(context):
    context.app.search_results_page.click_add_cart()

    # context.driver.execute_script("window.scrollTo(0, 490)")
    # context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart btn
    # context.driver.wait.until(
    #     EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
    #     message='Side navigation product name not visible'
    # )
    #
    # sleep(5)
