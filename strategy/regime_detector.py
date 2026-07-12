class RegimeDetector:


    def analyze(self, indicators):


        adx = indicators.get(
            "adx",
            0
        )


        atr = indicators.get(
            "atr",
            0
        )


        if adx > 25:

            regime = "TRENDING"


        elif atr > 0:

            regime = "VOLATILE"


        else:

            regime = "RANGING"



        return {


            "market_regime": regime


        }