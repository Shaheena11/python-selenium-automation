from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver

SEARCH_INPUT = (By.ID,'search')
SEARCH_SUBMIT = (By.CSS_SELECTOR, "button[aria-label='search']")

@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    # search = context.driver.find_element(*SEARCH_INPUT)
    search = context.driver.wait.until(EC.visibility_of_element_located(SEARCH_INPUT))
    search.clear()
    search.send_keys(search_word)
    #
    # element = context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT))
    # element.click()


@when('Click on search icon')
def click_search_icon(context):
    # context.driver.find_element(*SEARCH_SUBMIT).click()
    element = context.driver.wait.until(EC.element_to_be_clickable(SEARCH_SUBMIT))
    element.click()


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    search_word = search_word.lower()
    current_url = context.driver.current_url.lower()
    assert search_word in current_url, f'Expected query not in {current_url}'
