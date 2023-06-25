from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 450
TWITTER_EMAIL = 'rishi__1804'
TWITTER_PASSWORD = 'Spinjitzu@4'

class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=Service(executable_path="C:\Development\chromedriver.exe", log_path="NUL"))

        self.down = 0


    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(5)
        go_btn = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        go_btn.click()
        time.sleep(120)

        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        self.download_speed = float(self.down)
        return self.download_speed

    
    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D')
        time.sleep(3)

        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_btn.click()
        time.sleep(2)

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        login_btn.click()
        time.sleep(5)

        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet_btn.click()
        time.sleep(2)

        tweet_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
        tweet_input.send_keys(f'Hey @ACTFibernet why is my internet speed {self.down}down/ when I pay for {PROMISED_DOWN}down?')
        time.sleep(2)

        send_tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
        send_tweet_btn.click()


bot = InternetSpeedTwitterBot()

get_speed = bot.get_internet_speed()

if get_speed < PROMISED_DOWN:
    bot.tweet_at_provider()