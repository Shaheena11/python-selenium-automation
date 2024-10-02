from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By


# @given('Open sign in page')
# def open_sign_in(context):
#     context.app.sign_in_page.open_sign_in()

@when('Store original window')
def store_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()

@when('Click on Target terms and conditions link')
def click_t_and_c_link(context):
    context.app.sign_in_page.click_t_and_c_link()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.sign_in_page.verify_terms_and_conditions_page()

@then('User can close new window and switch back to original')
def User_close_new_window(context):
    context.app.sign_in_page.switch_to_window_by_id(context.original_window)
