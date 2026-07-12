from analytics.statistics import Statistics


class WeeklyReport:


    def __init__(self):

        self.stats = Statistics()



    def generate(self):


        summary = self.stats.get_summary()



        report = f"""

==================================================
📈 RIO AI FUTURES WEEKLY REPORT
==================================================

Trade           : {summary.get("trade",0)}

Win             : {summary.get("win",0)}

Loss            : {summary.get("loss",0)}

Win Rate        : {summary.get("win_rate",0):.2f} %

Net Profit      : {summary.get("net_profit",0)}

Profit Factor   : {summary.get("profit_factor",0)}

Max Drawdown    : {summary.get("max_drawdown",0)}

Sharpe Ratio    : {summary.get("sharpe_ratio",0)}

==================================================

"""

        return report