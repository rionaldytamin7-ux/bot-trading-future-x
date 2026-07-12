class FeatureEngine:

    def build(
        self,
        market,
        pattern,
        context,
        mtf,
        trade
    ):

        return {

            "market_regime":
                market["market_regime"],

            "volume_status":
                market["volume_status"],

            "btc_dominance":
                context["btc_dominance"],

            "funding_rate":
                context["funding_rate"],

            "open_interest":
                context["open_interest"],

            "pattern":
                pattern["primary_pattern"],

            "pattern_score":
                pattern["confidence"],

            "trend_4h":
                mtf["trend_4h"],

            "trend_1h":
                mtf["trend_1h"],

            "trend_15m":
                mtf["trend_15m"],

            "entry_side":
                trade["side"],

            "risk_reward":
                trade["risk_reward"],

            "leverage":
                trade["leverage"]

        }