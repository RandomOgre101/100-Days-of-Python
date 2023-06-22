from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path="C:\Development\chromedriver.exe", log_path="NUL"))

EMAIL = 'daxsteel1234@gmail.com'
PASSWORD = 'spinitzu'

driver.get('https://tinder.com/')
time.sleep(3)

login_btn = driver.find_element(By.XPATH, '//*[@id="q-971264251"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_btn.click()
time.sleep(5)


fb_btn = driver.find_element(By.XPATH, '//*[@id="q1595321969"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div')
fb_btn.click()
