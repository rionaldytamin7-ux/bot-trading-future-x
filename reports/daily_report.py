from analytics.statistics import Statistics


class DailyReport:


    def __init__(self):

        self.stats = Statistics()



    def generate(self):


        summary = self.stats.get_summary()



        report = f"""

==================================================
📊 RIO AI FUTURES DAILY REPORT
==================================================

Trade          : {summary.get("trade",0)}

Win            : {summary.get("win",0)}

Loss           : {summary.get("loss",0)}

Win Rate       : {summary.get("win_rate",0):.2f} %

Total Profit   : {summary.get("profit",0)}

Total Loss     : {summary.get("loss_amount",0)}

Net Profit     : {summary.get("net_profit",0)}

==================================================

"""


        return report