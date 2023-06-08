import requests
from twilio.rest import Client

TWILIO_SID = ""
TWILIO_TOKEN = ""

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