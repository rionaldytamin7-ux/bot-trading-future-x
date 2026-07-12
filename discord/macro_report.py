from macro.summary import get_macro
from macro.etf import format_money


def build_macro_report():

    macro = get_macro()

    etf = macro["etf"]

    btc = etf["btc"]

    report = f"""🌍 **DAILY MACRO REPORT**

📊 **MARKET**
DXY: {macro["dxy"]} | NASDAQ: {macro["nasdaq"]} | S&P500: {macro["sp500"]}
BTC DOM: {macro["btc_dom"]} | ALT DOM: {macro["alt_dom"]}
━━━━━━━━━━━━━━━━━━━━━━
🟠 **BTC ETF**
{btc["last3"][2]["date"]}  {format_money(btc["last3"][2]["total"])}
{btc["last3"][1]["date"]}  {format_money(btc["last3"][1]["total"])}
{btc["last3"][0]["date"]}  {format_money(btc["last3"][0]["total"])}

5D: {format_money(btc["5d"])} | 30D: {format_money(btc["30d"])}
IBIT: {format_money(btc["today"]["etf1"])} | FBTC: {format_money(btc["today"]["etf2"])}
━━━━━━━━━━━━━━━━━━━━━━
🔵 **ETH ETF**
{etf["eth"]["last3"][2]["date"]}  {format_money(etf["eth"]["last3"][2]["total"])}
{etf["eth"]["last3"][1]["date"]}  {format_money(etf["eth"]["last3"][1]["total"])}
{etf["eth"]["last3"][0]["date"]}  {format_money(etf["eth"]["last3"][0]["total"])}

5D: {format_money(etf["eth"]["5d"])} | 30D: {format_money(etf["eth"]["30d"])}
ETHA: {format_money(etf["eth"]["today"]["etf1"])} | FETH: {format_money(etf["eth"]["today"]["etf2"])}
━━━━━━━━━━━━━━━━━━━━━━
🇺🇸 **ECONOMY**
CPI  | Cur: {macro["cpi_current"]} | Prev: {macro["cpi_previous"]} | Act: {macro["cpi_actual"]:+.2f}%

PPI  | Cur: {macro["ppi_current"]} | Prev: {macro["ppi_previous"]} | Act: {macro["ppi_actual"]:+.2f}%
"""
    return report


if __name__ == "__main__":

    print(build_macro_report())