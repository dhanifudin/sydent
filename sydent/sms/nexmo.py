import nexmo
from twisted.internet import defer


class NexmoSMS:
    def __init__(self, sydent):
        self.sydent = sydent

    @defer.inlineCallbacks
    def sendTextSMS(self, body, dest, source=None):
        api_key = self.sydent.cfg.get('sms', 'key')
        api_secret = self.sydent.cfg.get('sms', 'secret')

        nexmo_client = nexmo.Client(
            api_key, api_secret
        )

        response = nexmo_client.send_message({
            'from': source,
            'to': dest,
            'text': body
        })

        if response is None:
            raise Exception("Failed to send SMS OTP")
