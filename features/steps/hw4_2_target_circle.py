

from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

BOXES = (By.CSS_SELECTOR, 'div[data-component="Cells Component Container"] div[class="cell-item-content"]')
# open the url
@given('Open Target Circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')
    sleep(6)


@then('Verify 10 cells')
def verify_cells(context):
    expected_amount = 10
    links = context.driver.find_elements(*BOXES)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
