import requests
from twilio.rest import Client

TWILIO_SID = "ACe43edbd9e7497672d0644e9b64cc5706"
TWILIO_TOKEN = "e3d398542ae3f8f5fc5a02e26ead8b52"

class NotificationManager:
    
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_message(self, message):
        message = self.client.messages.create(
        body=message,
        from_="+13612735690",
        to="+919600191653"
        )
        print(message.sid)