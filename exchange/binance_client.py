from binance.client import Client

from config import Config


class BinanceClient:

    def __init__(self):

        self.client = Client(
            api_key=Config.BINANCE_API_KEY,
            api_secret=Config.BINANCE_SECRET_KEY
        )

        if Config.MODE.lower() == "testnet":
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client

    def ping(self):
        return self.client.ping()

    def server_time(self):
        return self.client.get_server_time()