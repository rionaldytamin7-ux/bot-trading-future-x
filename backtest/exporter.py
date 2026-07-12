import pandas as pd


class BacktestExporter:


    def export_csv(

        self,

        trades,

        filename="backtest_result.csv"

    ):

        df = pd.DataFrame(trades)

        df.to_csv(

            filename,

            index=False

        )

        return filename



    def export_excel(

        self,

        trades,

        filename="backtest_result.xlsx"

    ):

        df = pd.DataFrame(trades)

        df.to_excel(

            filename,

            index=False

        )

        return filename