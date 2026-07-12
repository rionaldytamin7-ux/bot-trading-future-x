from backtest.equity import EquityCurve
import math


class BacktestMetrics:
    def calculate(
        self,
        trades
    ):


        total = len(
            trades)

        # ==========================
        # WIN / LOSS LIST
        # ==========================

        win_trades = [
            trade
            for trade in trades
            if trade["result"] == "WIN"]

        loss_trades = [
            trade
            for trade in trades
            if trade["result"] == "LOSS"]

        win = len(
            [
                x for x in trades
                if x["result"]=="WIN"
            ])
        
        loss = len(
            [
                x for x in trades
                if x["result"]=="LOSS"
            ])

        # ==========================
        # GROSS PROFIT
        # ==========================
        gross_profit = sum(
            trade["pnl"]
            for trade in win_trades
        )

        gross_loss = abs(
            sum(
                trade["pnl"]
                for trade in loss_trades
            )
        )

        # ==========================
        # AVERAGE
        # ==========================
        average_win = (
            gross_profit /
            len(win_trades)
        ) if win_trades else 0

        average_loss = (
            gross_loss /
            len(loss_trades)
        ) if loss_trades else 0

        # ==========================
        # PROFIT FACTOR
        # ==========================
        if gross_loss > 0:
            profit_factor = (
                gross_profit /
                gross_loss)
        else:
            profit_factor = 0

        # ==========================
        # EXPECTANCY
        # ==========================
        expectancy = (
            pnl /total ) if total else 0


        if total:
            win_rate = (
                win / total) * 100

        else:
            win_rate = 0

        pnl = sum(
            x["pnl"]
            for x in trades)
        
        equity = EquityCurve()

        history = equity.calculate(trades)

        sharpe = self.calculate_sharpe(
            trades
        )

        sortino = self.calculate_sortino(
            trades
        )

        calmar = self.calculate_calmar(

            roi,

            max_drawdown

        )

        cagr = self.calculate_cagr(

            initial_balance,

            final_balance

        )

        recovery = self.calculate_recovery(pnl,max_drawdown)
        
        max_drawdown = equity.max_drawdown(history)

        return {
            "trade":
            total,
            "win":

            win,
            "loss":

            loss,
            "win_rate":

            round(
                win_rate,
                2),

            "pnl":

            round(pnl,2),

            "equity_curve": history}

    def calculate_sharpe(
        self,
        trades
    ):

        if len(trades) < 2:
            return 0

        returns = [

            trade["pnl"]

            for trade in trades

        ]

        average = sum(returns) / len(returns)

        variance = sum(

            (x-average)**2

            for x in returns

        ) / len(returns)

        std = math.sqrt(variance)

        if std == 0:
            return 0

        return round(

            average/std,

            2)
    
#SORTINO
    def calculate_sortino(
        self,
        trades
    ):

        if len(trades) < 2:
            return 0

        returns = [

            trade["pnl"]

            for trade in trades

        ]

        average = sum(returns)/len(returns)

        downside = [

            x

            for x in returns

            if x < 0

        ]

        if len(downside) == 0:
            return 0

        variance = sum(

            x*x

            for x in downside

        ) / len(downside)

        downside_std = math.sqrt(variance)

        if downside_std == 0:
            return 0

        return round(

            average /

            downside_std,

            2

        )
#CALMAR

    def calculate_calmar(

        self,

        roi,

        drawdown

    ):

        if drawdown == 0:

            return 0

        return round(

            roi /

            drawdown,

            2

        )
#CAGR

    def calculate_cagr(

        self,

        initial_balance,

        final_balance,

        years=1

    ):

        if initial_balance <= 0:

            return 0

        cagr = (

            (

                final_balance /

                initial_balance

            )

            **

            (

                1/years

            )

        ) - 1

        return round(

            cagr*100,

            2

        )
#recovery 

    def calculate_recovery(

        self,

        net_profit,

        drawdown

    ):

        if drawdown == 0:

            return 0

        return round(

            net_profit /

            drawdown,

            2

        )


    metrics = {

        "initial_balance":1000,

        "final_balance":1000+pnl,

        "net_profit":pnl,

        "roi":0,

        "trade":total,

        "win":win,

        "loss":loss,

        "win_rate":win_rate,

        "average_profit":round(average_win,2),

        "average_loss":round(average_loss,2),

        "largest_win":0,

        "largest_loss":0,

        "profit_factor":round(profit_factor,2),

        "expectancy":round(expectancy,2),

        "max_drawdown":max_drawdown,

        "sharpe_ratio":sharpe,

        "sortino_ratio":sortino,

        "calmar_ratio":calmar,

        "cagr":cagr,

        "recovery_factor":recovery,

        "average_holding":0,

        "leverage":10

    }