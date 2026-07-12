"""
RIO AI FUTURES
Signal Engine

Mengolah hasil indikator
menjadi keputusan market.

"""

from core.logger import get_logger


logger = get_logger()


class SignalEngine:


    def __init__(self):

        pass



    def analyze(self, indicators):

        score = 0


        # EMA TREND

        if indicators["ema20"] > indicators["ema50"]:

            score += 1

        else:

            score -= 1



        # RSI

        if indicators.get("rsi"):

            if indicators["rsi"] > 50:

                score += 1

            else:

                score -= 1



        # MACD

        if indicators.get("macd"):

            if indicators["macd"] > 0:

                score += 1

            else:

                score -= 1



        # RESULT


        if score >= 2:

            signal = "LONG"


        elif score <= -2:

            signal = "SHORT"


        else:

            signal = "WAIT"



        return {

            "signal": signal,

            "score": score

        }