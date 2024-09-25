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
    context.driver.execute_script("window.scrollTo(0, 490)")
    sleep(10)
   # context.driver.find_element(By.ID,"addToCartButtonOrTextIdFor13376546").click()
    # context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor12954155").click()
    context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor12954155").click()
    context.driver.find_element(By.XPATH, "//div[@class='sc-529a2ea7-0 hbiLND']//div//button[@id='addToCartButtonOrTextIdFor12954155']").click()  #Add Cart from Side navigation

    # context.driver.find_element(By.CSS_SELECTOR,"button[id*='addToCartButton']").click()
    sleep(5)

@when ('Open my cart page')
def click_view_cart(context):
    # context.driver.find_element(By.XPATH, "//button[@data-test='orderPickupButton']").click()
    sleep(3)
    context.driver.find_element(By.CSS_SELECTOR, "a[class='sc-ddc722c0-0 sc-3d5333d1-0 jKTcnK hhYRAp']").click()
    sleep(5)

@then('Verify cart has {number} product')
def verify_cart(context, number):
    total_in_cart = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
    assert f'{number} item' in total_in_cart, f"Expected {number} item but got {total_in_cart}"