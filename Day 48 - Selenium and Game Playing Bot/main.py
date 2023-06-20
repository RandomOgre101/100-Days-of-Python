from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path="C:\Development\chromedriver.exe", log_path="NUL"))

driver.get("https://www.python.org")

# # search_bar = driver.find_element(By.NAME, 'q')
# # print(search_bar.tag_name)
# # print(search_bar.get_attribute("placeholder"))

# documentation_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(documentation_link.text)

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery ul")[0].text.split("\n")

info_pairs = []

for i in range(0, len(events), 2):
    pair = (events[i], events[i + 1])
    info_pairs.append(pair)

final={}
for i in range(0,len(info_pairs)):
    final[i] = {'date': info_pairs[i][0], 'name': info_pairs[i][1]}

print(final)


driver.quit()