from pushover import Client
from .creds import get_creds
from operator import itemgetter


class PushoverClient:
    def __init__(self):
        token, key = itemgetter("pushover_api_token", "pushover_user_key")(get_creds())
        self._cli = Client(key, api_token=token)

    def send_message(self, message, title="New TV Show Episode Added"):
        return self._cli.send_message(message=message, title=title)
