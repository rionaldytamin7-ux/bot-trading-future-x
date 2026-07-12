from ta.trend import ADXIndicator


class ADX:


    @staticmethod
    def calculate(df):

        adx = ADXIndicator(

            high=df["high"],

            low=df["low"],

            close=df["close"],

            window=14

        )


        df["adx"] = adx.adx()


        return {

            "adx": df["adx"].iloc[-1]

        }