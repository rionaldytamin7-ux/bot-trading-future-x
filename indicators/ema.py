from ta.trend import EMAIndicator


class EMA:

    @staticmethod
    def calculate(df):

        df["ema20"] = EMAIndicator(
            df["close"],
            window=20
        ).ema_indicator()

        df["ema50"] = EMAIndicator(
            df["close"],
            window=50
        ).ema_indicator()

        return {

            "ema20": df["ema20"].iloc[-1],

            "ema50": df["ema50"].iloc[-1]

        }