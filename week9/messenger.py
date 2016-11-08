from twilio.rest import TwilioRestClient


class Messenger:
    account_sid = "ACff0caeefc47a12d87e8ebf519d93431d"
    auth_token  = "06ebc1380d39b59bf754c4d51397ae0e"

    def __init__(self):
        self.client = TwilioRestClient(self.account_sid, self.auth_token)

    def send(self, message):
        self.message = self.client.messages.create(body=message, to="+18645618074", from_="+18645010618")
