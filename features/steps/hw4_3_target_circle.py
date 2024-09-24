from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By


@when('Search for {item}')
def search_products(context, item):
    context.driver.find_element(By.ID,"search").send_keys(item)
    context.driver.find_element(By.XPATH,"//input[@id='search']").click()
    sleep(15)

@when('Click on Add to Cart Button')
def click_add_cart(context):
    # context.driver.execute_script("window.scrollTo(0, 500);")
    # context.driver.find_element(By.ID,"addToCartButtonOrTextIdFor52001650").click()
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
    sleep(3)