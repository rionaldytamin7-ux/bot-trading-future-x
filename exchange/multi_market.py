from exchange.market import Market

class MultiTimeframe:

    def __init__(self):
       
        self.market = Market()

    def get_multi_data(self, symbol):


        timeframes = [
            "1m",
            "5m",
            "15m",
            "1h",
            "4h"
        ]


        data = {}

        for tf in timeframes:

            data[tf] = self.market.get_dataframe(

                symbol,

                tf,

                200

            )

        return data