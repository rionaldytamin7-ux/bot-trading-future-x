from binance.client import Client

client = Client(

    Config.BINANCE_API_KEY,

    Config.BINANCE_SECRET_KEY,

    testnet=Config.TESTNET

)

def ping(self):

    return self.client.ping()

def server_time(self):

    return self.client.get_server_time()

def account(self):

    return self.client.futures_account()

def balance(self):

    return self.client.futures_account_balance()

def positions(self):

    return self.client.futures_position_information()

class SymbolFilter:

    def __init__(self, client):
        self.client = client
        self.cache = {}

    def get_filter(self, symbol):

        if symbol in self.cache:
            return self.cache[symbol]

        info = self.client.futures_exchange_info()

        for s in info["symbols"]:
            if s["symbol"] == symbol:

                self.cache[symbol] = s
                return s

        return None
    
    def normalize_quantity(self, symbol, quantity):

        info = self.get_filter(symbol)

        lot = next(
            f for f in info["filters"]
            if f["filterType"] == "LOT_SIZE"
        )

        step = float(lot["stepSize"])

        precision = len(str(step).split(".")[1].rstrip("0"))

        return round(quantity, precision)
    
    def normalize_price(self, symbol, price):

        info = self.get_filter(symbol)

        tick = next(
            f for f in info["filters"]
            if f["filterType"] == "PRICE_FILTER"
        )

        tick_size = float(tick["tickSize"])

        precision = len(str(tick_size).split(".")[1].rstrip("0"))

        return round(price, precision)
    
