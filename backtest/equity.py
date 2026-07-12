class EquityCurve:

    def __init__(
        self,
        initial_balance=1000):
        self.initial_balance = initial_balance

    def calculate(
        self,
        trades):

        balance = self.initial_balance
        history = []

        for index, trade in enumerate(trades, start=1):
            balance += trade["pnl"]

            history.append({
                "trade": index,
                "balance": round(balance,2),
                "pnl": round(trade["pnl"],2),
                "result": trade["result"]})
        return history

#ISI EQUITAS            
    def max_drawdown(

        self,

        history

    ):


        if not history:

            return 0


        peak = history[0]["balance"]

        max_dd = 0


        for item in history:


            balance = item["balance"]


            if balance > peak:

                peak = balance


            drawdown = (

                (peak - balance)

                / peak

            ) * 100


            if drawdown > max_dd:

                max_dd = drawdown


        return round(

            max_dd,

            2

        )
