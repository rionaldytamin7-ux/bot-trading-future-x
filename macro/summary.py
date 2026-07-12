import requests
import yfinance as yf

from macro.etf import get_etf
from macro.economy import get_economy

def yahoo_change(ticker):
    try:
        df = yf.Ticker(ticker).history(period="2d")

        last = float(df["Close"].iloc[-1])
        prev = float(df["Close"].iloc[-2])

        change = (last - prev) / prev * 100

        return last, change

    except:
        return None, None


def get_macro():

    macro = {}
    
    # ---------------- DXY ----------------

    last, chg = yahoo_change("DX-Y.NYB")

    if last is not None:
        macro["dxy"] = f"{last:.2f} ({chg:+.2f}%)"
    else:
        macro["dxy"] = "-"

    # ---------------- NASDAQ ----------------

    last, chg = yahoo_change("^IXIC")

    if last is not None:
        macro["nasdaq"] = f"{chg:+.2f}%"
    else:
        macro["nasdaq"] = "-"

    # ---------------- SP500 ----------------

    last, chg = yahoo_change("^GSPC")

    if last is not None:
        macro["sp500"] = f"{chg:+.2f}%"
    else:
        macro["sp500"] = "-"

    # ---------------- Fear & Greed ----------------

    try:
        fg = requests.get(
            "https://api.alternative.me/fng/",
            timeout=5
        ).json()["data"][0]

        macro["fear"] = f'{fg["value"]} ({fg["value_classification"]})'

    except:
        macro["fear"] = "-"

    # ---------------- CoinGecko ----------------

    try:

        data = requests.get(
            "https://api.coingecko.com/api/v3/global",
            timeout=5
        ).json()["data"]

        btc = data["market_cap_percentage"]["btc"]

        macro["btc_dom"] = f"{btc:.2f}%"

        macro["alt_dom"] = f"{100-btc:.2f}%"

    except:

        macro["btc_dom"] = "-"
        macro["alt_dom"] = "-"

    # ETF
    

    macro["etf"] = get_etf()
    # CPI PPI

    macro.update(get_economy())
    
    return macro