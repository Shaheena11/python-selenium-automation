from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_EMPTY = (By.CSS_SELECTOR, "div[class='sc-5da3fdcc-0 ChXCV']")

@given('Open target main page')
def open_main(context):
    # context.driver.get('http://www.target.com/')
    context.app.main_page.open_main()

@when('Click on cart icon')
def click_cart(context):
    # context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartLink"]').click()
    context.app.main_page.click_cart()

@then('Verify “Your cart is empty” message is shown')
def verify_cart_is_empty(context):
    context.app.main_page.cart_is_empty()
    # actual_result = context.driver.find_element(*CART_EMPTY).text
    # expected_result = 'Your cart is empty'
    # assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'

@when('Search for {item}')
def search_product(context, item):
    context.app.header.search_product(item)

    # # print(item)
    # # Search field => enter tea
    # context.driver.find_element(By.ID,'search').send_keys(item)
    # # Search button => click
    # context.driver.find_element(By.XPATH, '//button[@data-test='@web/Search  '' ).click()
    # sleep(8)


@then('Verify header has {expected_amount} links')
def verify_header(context, expected_amount):
    expected_amount = int(expected_amount) # '6' => 6
    links = context.driver.find_elements(By.CSS_SELECTOR, '[data-test*="@web/GlobalHeader   "]')
    assert len(links) == expected_amount, f'Expected {expected_amount} links, got {len(links)}'


@then('Verify header is shown')
def verify_header(context):
    context.driver.finf_element(By.CSS_SELECTOR, "[class*='styles_utilityHeaderContaine']").click()