import requests
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_KEY = "N21c0-INfwr5pVycTrR-5ebzDkFXmuEa"

today = datetime.now().strftime("%d/%m/%Y")
plus_30 = (datetime.strptime(today, "%d/%m/%Y") + timedelta(days = 6*30)).strftime("%d/%m/%Y")