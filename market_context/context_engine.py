"""
RIO AI FUTURES

Market Context Engine

Membaca kondisi pasar global

"""


from market_context.macro_adapter import MacroAdapter


class MarketContextEngine:

    def __init__(self):
        self.macro = MacroAdapter()

    def analyze(self, market_data):
        macro_data = self.macro.get_macro_data()

        context = {

            "market_state":
            "NEUTRAL",


            "risk_mode":
            "NORMAL",


            "alt_rotation":
            False,


            "macro":
            macro_data
        }

        # ======================
        # BTC MARKET CONDITION
        # ======================
        btc_trend = market_data.get(
            "btc_trend")

        if btc_trend == "BULLISH":
            context["market_state"] = "RISK_ON"

        elif btc_trend == "BEARISH":
            context["market_state"] = "RISK_OFF"

        # ======================
        # ALT ROTATION
        # ======================
        btc_dom = market_data.get(
            "btc_dominance")
        eth_btc = market_data.get(
            "eth_btc")

        if (
            btc_dom == "DOWN"
            and
            eth_btc == "UP"):

            context["alt_rotation"] = True

        # ======================
        # RISK CONTROL
        # ======================
        if (
            context["market_state"]
            ==
            "RISK_OFF"):
            context["risk_mode"] = "DEFENSIVE"

        return context