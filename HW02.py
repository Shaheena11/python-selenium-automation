from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
#driver_path = ChromeDriverManager().install()
driver_path = '/Users/Shaheena/Desktop/python-selenium-automation/chromedriver'
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fsign%2Fs%3Fk%3Dsign%2Bin%26ref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(5)

#Amazon logo
driver.find_element(By.XPATH, "//i[@role='img']")

#driver.find_element(By.ID,'ap_email')


#email field
driver.find_element(By.XPATH, "//input[@type='email']")

#Continue button
driver.find_element(By.XPATH, "//input[@id='continue']")

#Privacy Notice link (select element by tag and partial attribute value)
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/help/customer')]")

#Need help link (select element by tag and partial attribute value)
driver.find_element(By.XPATH, "//span[contains(@class, 'a-expander')]")

#Forgot your password link (select element by tag and partial attribute value)
driver.find_element(By.XPATH,"//a[contains(@id, 'auth-')]")

#Other issues with Sign-In link (select element by tag and partial attribute value)
driver.find_element(By.XPATH,"//a[contains(@id, 'ap-other')]")

#Creat your Amazon account button
driver.find_element(By.XPATH,"//a[contains(@id, 'createAccount')]")


driver.quit()

# Home work #2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
#driver_path = ChromeDriverManager().install()
driver_path = '/Users/Shaheena/Desktop/python-selenium-automation/chromedriver'
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
#
driver.get('https://www.target.com/')

driver.find_element(By.XPATH,"//a[@data-test = '@web/AccountLink']//span[text()='Sign in']").click()
#driver.find_element(By.XPATH,"//button[@type='button']").click()

#click signin from side navigation
driver.find_element(By.XPATH,"//a[@data-test='accountNav-signIn']").click()

# Verify "Sign into your Target account" text is shown

expected = 'Sign into your Target account'
sleep(5)
actual = driver.find_element(By.XPATH,"//span").text
assert expected == actual, f'Expected {expected} did not match {actual}'
#assert expected_text in actual_text, f'Expected text {expected_text} is in actual text {actual_text}'

# Verify the SignIn button is shown
driver.find_element(By.ID, "login")


