import requests
from twilio.rest import Client

account_sid = 'SID'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

api_key = "API_KEY"
endpoint = "https://api.openweathermap.org/data/3.0/onecall"
parameters = {
    "lat": 13.082680,
    "lon": 80.270721,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

r = requests.get(url=endpoint, params=parameters)
r.raise_for_status()
weather_data = r.json()

will_rain = False

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    code = hour_data["weather"][0]["id"]
    if int(code) < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
    from_='number',
    body="It's going to rain",
    to='number'
    )