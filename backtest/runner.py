from backtest.data_loader import BacktestDataLoader

from backtest.engine import BacktestEngine

from backtest.metrics import BacktestMetrics

from backtest.strategy_adapter import BacktestStrategy

from backtest.report import BacktestReport

from backtest.exporter import BacktestExporter

class BacktestRunner:



    def __init__(self):

        self.loader = BacktestDataLoader()

        self.engine = BacktestEngine()

        self.metrics = BacktestMetrics()

        self.exporter = BacktestExporter()


    def run(

        self,

        symbol="BTCUSDT",

        timeframe="1h"

    ):



        df = self.loader.load(

            symbol,

            timeframe

        )

        strategy_engine = BacktestStrategy()

#Old ver :
        # def test_strategy(data):
        #     close = data["close"].iloc[-1]
        #     previous = data["close"].iloc[-2]

            # if close > previous:
            #     return "LONG"
            # return "WAIT"

        def test_strategy(data):

            result = strategy_engine.analyze(data)
            return result["decision"]


        trades = self.engine.run(
            df,
            test_strategy)
        self.exporter.export_csv(
            trades
        )

        self.exporter.export_excel(
            trades
        )
        
        result = self.metrics.calculate(trades)

        report = BacktestReport()

#UPDATE VER 1.2
        return report.generate(
            result,
            symbol,
            timeframe,
            "AUTO",
            "AUTO")

        return result