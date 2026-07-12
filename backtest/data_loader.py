from exchange.client import BinanceClient
import pandas as pd


class BacktestDataLoader:


    def __init__(self):

        self.client = BinanceClient()



    def load(

        self,

        symbol,

        interval,

        limit=1000

    ):


        candles = self.client.get_klines(

            symbol,

            interval,

            limit

        )


        df = pd.DataFrame(

            candles,

            columns=[

                "open_time",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "close_time",
                "quote_volume",
                "trade_count",
                "taker_buy_base",
                "taker_buy_quote",
                "ignore"

            ]

        )


        numeric_columns = [

            "open",
            "high",
            "low",
            "close",
            "volume"

        ]


        for col in numeric_columns:

            df[col] = df[col].astype(float)



        return df