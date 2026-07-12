from exchange.binance_client import BinanceClient


class Account:

    def __init__(self):

        self.client = BinanceClient().get_client()

    def get_server_time(self):

        return self.client.get_server_time()

    def get_account_info(self):

        return self.client.futures_account()

    def get_balance(self):

        return self.client.futures_account_balance()

    def get_positions(self):

        return self.client.futures_position_information()