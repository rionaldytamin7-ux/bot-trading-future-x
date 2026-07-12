from ta.volatility import BollingerBands


class Bollinger:


    @staticmethod
    def calculate(df):

        bb = BollingerBands(

            close=df["close"],

            window=20,

            window_dev=2

        )


        df["bb_high"] = bb.bollinger_hband()

        df["bb_low"] = bb.bollinger_lband()

        df["bb_mid"] = bb.bollinger_mavg()


        return {

            "bb_high":
            df["bb_high"].iloc[-1],

            "bb_low":
            df["bb_low"].iloc[-1],

            "bb_mid":
            df["bb_mid"].iloc[-1]

        }