from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_path = '/Users/Shaheena/Desktop/python-selenium-automation/chromedriver'
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(15)

#Amazon locators
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")
#Creat Account locator
driver.find_element(By.CSS_SELECTOR, ".a-spacing-small")
# your name
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
# email
driver.find_element(By.CSS_SELECTOR, "#ap_email")
# password
driver.find_element(By.CSS_SELECTOR, "#ap_password")
# passwords must be 6 characters
driver.find_element(By.CSS_SELECTOR, ".a-alert-content")
# re-enter password
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
# continue locator
driver.find_element(By.CSS_SELECTOR, "#continue")
# conditions of Use
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']")
# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']")
# sign in locator
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")