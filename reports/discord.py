import requests

from config import Config


class DiscordReporter:

    def __init__(self):
        self.webhook = Config.DISCORD_WEBHOOK

    def send_message(self, message: str):

        if not self.webhook:
            return

        payload = {
            "content": message
        }

        requests.post(
            self.webhook,
            json=payload,
            timeout=10
        )