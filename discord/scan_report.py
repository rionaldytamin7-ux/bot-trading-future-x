from core.runner import analyze
from config.watchlist import WATCHLIST
from tabulate import tabulate

def build_scan_report():

    result = []

    for coin in WATCHLIST:

        try:
            result.append(analyze(coin))
        except:
            pass

    result.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    table = []

    for i, item in enumerate(result[:10], 1):

        table.append([
            i,
            item["coin"],
            item["signal"],
            item["trade"]["entry"],
            item["trade"]["tp1"],
            item["trade"]["tp2"],
            item["trade"]["sl"],
            item["risk"]["leverage"]
        ])

    txt = tabulate(
        table,
        headers=[
            "#",
            "Coin",
            "Signal",
            "Entry",
            "TP1",
            "TP2",
            "SL",
            "Lev"
        ],
        tablefmt="pretty"
    )

    return txt