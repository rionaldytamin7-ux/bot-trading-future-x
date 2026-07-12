from ta.trend import MACD as MACDIndicator


class MACD:


    @staticmethod
    def calculate(df):

        macd = MACDIndicator(
            close=df["close"]
        )


        df["macd"] = macd.macd()

        df["macd_signal"] = macd.macd_signal()


        return {

            "macd": df["macd"].iloc[-1],

            "macd_signal":
            df["macd_signal"].iloc[-1]

        }