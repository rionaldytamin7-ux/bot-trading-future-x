from backtest.simulator import BacktestSimulator



class BacktestEngine:


    def __init__(self):

        self.simulator = BacktestSimulator()



    def run(

        self,

        df,

        strategy

    ):


        result = self.simulator.run(

            df,

            strategy

        )


        return result