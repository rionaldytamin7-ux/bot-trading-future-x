from ta.volatility import AverageTrueRange


class ATR:


    @staticmethod
    def calculate(df):

        atr = AverageTrueRange(

            high=df["high"],

            low=df["low"],

            close=df["close"],

            window=14

        )


        df["atr"] = atr.average_true_range()


        return {

            "atr": df["atr"].iloc[-1]

        }