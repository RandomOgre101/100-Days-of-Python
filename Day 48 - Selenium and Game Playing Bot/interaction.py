from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path="C:\Development\chromedriver.exe", log_path="NUL"))

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# # article_count.click()

# edit = driver.find_element(By.LINK_TEXT, 'anyone can edit')
# # edit.click()

# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

driver.get('https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Rishi')

last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Ravichandran')

email_address = driver.find_element(By.NAME, 'email')
email_address.send_keys('daxsteel1234@gmail.com')

button = driver.find_element(By.CLASS_NAME, 'btn')
button.click()


# driver.quit()
