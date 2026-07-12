class AIScoring:


    def __init__(self):

        pass



    def calculate(self, data):


        score = 50



        # ======================
        # MARKET CONTEXT
        # ======================


        context = data.get(
            "market_context",
            {}
        )


        if context.get(
            "market_state"
        ) == "RISK_ON":

            score += 10



        elif context.get(
            "market_state"
        ) == "RISK_OFF":

            score -= 10



        # ======================
        # PATTERN
        # ======================


        pattern = data.get(
            "pattern",
            {}
        )


        confidence = pattern.get(
            "confidence",
            0
        )


        if confidence >= 80:

            score += 15


        elif confidence >= 60:

            score += 8



        # ======================
        # MULTI TIMEFRAME
        # ======================


        mtf = data.get(
            "multi_tf",
            {}
        )


        trend = mtf.get(
            "4h",
            {}
        ).get(
            "trend"
        )


        if trend == "BULLISH":

            score += 10


        elif trend == "BEARISH":

            score -= 10



        # ======================
        # VOLUME BEHAVIOR
        # ======================


        volume = data.get(
            "volume_status"
        )


        if volume == "HIGH":

            score += 5



        elif volume == "LOW":

            score -= 5



        # LIMIT

        score = max(
            0,
            min(
                score,
                100
            )
        )


        return score