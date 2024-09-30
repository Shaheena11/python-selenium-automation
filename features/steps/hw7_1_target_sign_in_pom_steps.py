from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@given('Open main page')
def Open_Main(context):
    context.app.main_page.open_main()

@when('Click on Sign In')
def Click_Sign_In(context):
    context.app.header.click_sign_in()

@then('From right side navigation menu click Sign In')
def Right_Ride_Click_Sign_In(context):
    context.app.header.right_side_click_sign_in()

@then('Verify Sign In form opened')
def Verify_Sign_In_From_Open(context):
    context.app.sign_in_page.verify_sign_in_from_open()
    # expected_result = 'Sign into your Target account'
    # actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    # assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
    # context.driver.find_element(By.ID, "login")
