from exchange.binance_client import BinanceClient
from utils.dataframe_engine import DataFrameEngine

class Market:

    def __init__(self):

        self.client = BinanceClient().get_client()

    def get_price(self, symbol):

        return self.client.futures_symbol_ticker(
            symbol=symbol
        )

    def get_book(self, symbol):

        return self.client.futures_order_book(
            symbol=symbol
        )

    def get_candles(

        self,

        symbol,

        interval,

        limit=500

    ):

        return self.client.futures_klines(

            symbol=symbol,

            interval=interval,

            limit=limit

        )
    
    def get_dataframe(
        self,
        symbol,
        interval,
        limit=500
    ):

        klines = self.get_candles(
            symbol,
            interval,
            limit
        )

        return DataFrameEngine.klines_to_dataframe(
        klines
        )