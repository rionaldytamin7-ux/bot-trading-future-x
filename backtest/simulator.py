class BacktestSimulator:


    def __init__(

        self,

        capital=1000,

        leverage=10

    ):

        self.capital = capital

        self.leverage = leverage



    def run(

        self,

        df,

        strategy

    ):


        trades = []


        for i in range(
            50,
            len(df)
        ):


            candle = df.iloc[i]



            signal = strategy(
                df.iloc[:i]
            )



            if signal == "LONG":

                entry = candle["close"]
                sl = entry * 0.98
                tp = entry * 1.04

                result = self.simulate_trade(
                    entry,
                    tp,
                    sl,
                    df.iloc[i:])
                
            elif signal == "SHORT":
                entry = candle["close"]
                sl = entry * 1.02
                tp = entry * 0.96

                result = self.simulate_short(
                    entry,
                    tp,
                    sl,
                    df.iloc[i:])

                trades.append(result)
        return trades


    def simulate_trade(
        self,
        entry,
        tp,
        sl,
        future ):

        for _, candle in future.iterrows():

            if candle["high"] >= tp:

                return {

                    "result":
                    "WIN",

                    "pnl":
                    (tp-entry)
                    *
                    self.leverage
                }

            if candle["low"] <= sl:
                return {
                    "result":
                    "LOSS",
                    "pnl":
                    (sl-entry)
                    *
                    self.leverage
                }
        return {
            "result":
            "OPEN",
            "pnl":0}
    
    def simulate_short(
        self,
        entry,
        tp,
        sl,
        future
    ):

        for _, candle in future.iterrows():
            if candle["low"] <= tp:

                return {
                    "result":"WIN",
                    "pnl":
                    (entry-tp)
                    *
                    self.leverage
                }

            if candle["high"] >= sl:

                return {
                    "result":"LOSS",
                    "pnl":
                    (entry-sl)
                    *
                    self.leverage
                }

        return {
            "result":"OPEN",
            "pnl":0

        }

