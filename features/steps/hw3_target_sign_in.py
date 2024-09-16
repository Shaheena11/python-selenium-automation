from lib2to3.fixes.fix_input import context

from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()
    sleep(2)

@then('From right side, click Sign In')
def right_side_click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()

@then('Verify sign in Target account')
def verify_sign_in_from_open(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
    context.driver.find_element(By.ID, "login")
