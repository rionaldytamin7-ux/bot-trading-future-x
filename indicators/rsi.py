from ta.momentum import RSIIndicator


class RSI:


    @staticmethod
    def calculate(df):

        df["rsi"] = RSIIndicator(
            close=df["close"],
            window=14
        ).rsi()


        return {

            "rsi": df["rsi"].iloc[-1]

        }