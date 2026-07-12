from backtest.runner import BacktestRunner
from analytics.statistics import Statistics

from reports.daily_report import DailyReport
from reports.weekly_report import WeeklyReport


class CommandEngine:


    def __init__(self):

        self.backtest = BacktestRunner()

        self.stats = Statistics()

        self.daily = DailyReport()

        self.weekly = WeeklyReport()



    def execute(

        self,

        command,

        *args

    ):


        command = command.lower()



        # ===========================
        # BACKTEST
        # ===========================

        if command == "backtest":


            symbol = args[0]

            timeframe = args[1]


            return self.backtest.run(

                symbol,

                timeframe

            )



        # ===========================
        # STATS
        # ===========================

        elif command == "stats":


            return self.stats.get_summary()



        # ===========================
        # DAILY
        # ===========================

        elif command == "daily":


            return self.daily.generate()



        # ===========================
        # WEEKLY
        # ===========================

        elif command == "weekly":


            return self.weekly.generate()



        return {

            "error":

            "Unknown Command"

        }