# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from time import sleep
#
#
# CART_EMPTY = (By.CSS_SELECTOR, "div[class='sc-5da3fdcc-0 ChXCV']")
#
# # open the url
# # @given('Open target page')
# # def open_main(context):
# #     context.driver.get('https://www.target.com/')
#
# # click on  => Cart
# @when('Click on Cart icon')
# def click_cart_icon(context):
#     context.driver.find_element(By.CSS_SELECTOR,"a[aria-label='cart 0 items']").click()
#     sleep(3)
#
# @then('Verify that cart is empty')
# def verify_cart_empty(context):
#     actual_result = context.driver.find_element(*CART_EMPTY).text
#     expected_result = 'Your cart is empty'
#     assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'