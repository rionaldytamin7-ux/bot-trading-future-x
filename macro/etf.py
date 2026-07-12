import requests
from bs4 import BeautifulSoup
from datetime import datetime

BTC_URL = "https://farside.co.uk/bitcoin-etf-flow-all-data/"

ETH_URL = "https://farside.co.uk/ethereum-etf-flow-all-data/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0 Safari/537.36",
    "Referer": "https://farside.co.uk/"
}


def parse_number(text):

    text = text.strip()

    if text == "" or text == "-":
        return 0.0

    text = text.replace(",", "")

    if "(" in text:
        text = "-" + text.replace("(", "").replace(")", "")

    return float(text)


def format_money(x):

    if abs(x) >= 1000:
        return f"{x/1000:+.2f}B"

    return f"{x:+.1f}M"


def get_flow(url, etf1, etf2):
    
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    tables = soup.find_all("table")

    table = None

    for t in tables:

        text = t.get_text(" ", strip=True)

        if etf1 in text and etf2 in text and "Total" in text:

            table = t

            break

    if table is None:
        raise Exception("ETF table tidak ditemukan")


    rows = table.find_all("tr")

    data = []

    for row in rows:

        cols = row.find_all("td")

        if len(cols) < 10:
            continue

        date_text = cols[0].get_text(" ", strip=True)

        try:

            datetime.strptime(date_text, "%d %b %Y")

        except:

            try:

                datetime.strptime(date_text, "%d %B %Y")

            except:

                continue
        
        data.append({

            "date": date_text,

            "etf1": parse_number(cols[1].text),

            "etf2": parse_number(cols[3].text),

            "total": parse_number(cols[-1].text)

        })

    if len(data) == 0:
        raise Exception("Data ETF tidak ditemukan.")


    valid = [x for x in data if x["total"] != 0]

    latest = valid[-1]

    last3 = valid[-3:]

    flow5 = sum(x["total"] for x in valid[-5:])

    flow30 = sum(x["total"] for x in valid[-30:])


    return {

        "today": latest,

        "last3": last3,

        "5d": flow5,

        "30d": flow30

    }

def get_etf():

    btc = get_flow(
        BTC_URL,
        "IBIT",
        "FBTC"
    )

    eth = get_flow(
        ETH_URL,
        "ETHA",
        "FETH"
    )

    return {

        "btc": btc,

        "eth": eth

    }

if __name__ == "__main__":

    etf = get_etf()

    print("=" * 40)
    print("BTC ETF")
    print("=" * 40)

    for row in reversed(etf["btc"]["last3"]):
        print(f'{row["date"]:12} {format_money(row["total"])}')

    print()

    print("5 Days :", format_money(etf["btc"]["5d"]))
    print("30 Days:", format_money(etf["btc"]["30d"]))

    print()

    print("IBIT :", format_money(etf["btc"]["today"]["etf1"]))
    print("FBTC :", format_money(etf["btc"]["today"]["etf2"]))

    print()
    print("=" * 40)
    print("ETH ETF")
    print("=" * 40)

    for row in reversed(etf["eth"]["last3"]):
        print(f'{row["date"]:12} {format_money(row["total"])}')

    print()

    print("5 Days :", format_money(etf["eth"]["5d"]))
    print("30 Days:", format_money(etf["eth"]["30d"]))

    print("ETHA :", format_money(etf["eth"]["today"]["etf1"]))
    print("FETH :", format_money(etf["eth"]["today"]["etf2"]))