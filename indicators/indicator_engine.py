from indicators.ema import EMA
from indicators.rsi import RSI
from indicators.macd import MACD
from indicators.atr import ATR
from indicators.adx import ADX
from indicators.bollinger import Bollinger
from indicators.volume import Volume

class IndicatorEngine:

    def __init__(self):
        pass

    def calculate(self, df):

        if len(df) < 100:

            return {
                "error": "Not enough candle data"
            }


        result = {}

        result.update(
            EMA.calculate(df)
        )

        result.update(
            RSI.calculate(df)
        )

        result.update(
            MACD.calculate(df)
        )

        result.update(
            ATR.calculate(df)
        )

        result.update(
            ADX.calculate(df)
        )

        result.update(
            Bollinger.calculate(df)
        )

        result.update(
            Volume.calculate(df)
        )

        return result