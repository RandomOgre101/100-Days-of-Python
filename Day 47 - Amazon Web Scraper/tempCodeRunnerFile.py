from bs4 import BeautifulSoup
import requests
import smtplib

my_email = 'rishitwt1804@gmail.com'
password = 'bgsmlereazqbkrti'

URL = "https://www.amazon.in/Razer-BlackWidow-V3-Mechanical-RZ03-03540100-R3M1/dp/B08G577XZF/ref=sr_1_3?crid=J1SWZVJA8UY6&keywords=razer+keyboard&qid=1687144362&sprefix=razer%2Caps%2C207&sr=8-3"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
}
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

price_as_list = soup.find(name='span', class_='a-price-whole').getText().split(".")[0].split(",")
price = [''.join(price_as_list)][0]
print(price)