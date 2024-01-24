from twilio.rest import Client

TWILIO_SID = "AC3dc4d93f088d7b8b4bf6b492ccce8475"
TWILIO_AUTH_TOKEN = "467daacbb54acff3014511076b1aea58"
TWILIO_VIRTUAL_NUMBER = "+18333563915"
TWILIO_VERIFIED_NUMBER = "+15054596727"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)
