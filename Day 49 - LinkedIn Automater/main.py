from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path="C:\Development\chromedriver.exe", log_path="NUL"))

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3625812506&f_AL=true&geoId=103644278&keywords=data%20analysis%20intern&location=United%20States&refresh=true')

time.sleep(2)

sign_in = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in.click()

username = driver.find_element(By.ID, 'username')
username.send_keys('--')

password = driver.find_element(By.ID, 'password')
password.send_keys('--')

btn = driver.find_element(By.CSS_SELECTOR, 'button')
btn.click()

time.sleep(5)

apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button')
apply_button.click()

time.sleep(5)

next_button = driver.find_element(By.ID, 'ember404')
next_button.click()

cover_letter_text = """
--
"""

cover_letter_box = driver.find_element(By.ID, 'multiline-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3625812506-2053103714989801866-text')
cover_letter_box.send_keys(cover_letter_text)
time.sleep(5)

review_button = driver.find_element(By.ID, 'ember410')
review_button.click()
time.sleep(3)

submit_button = driver.find_element(By.ID, 'ember420')
submit_button.click()
time.sleep(5)