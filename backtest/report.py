class BacktestReport:

    def generate(

        self,

        metrics,

        symbol,

        timeframe,

        start,

        end

    ):

        report = {

            "symbol": symbol,

            "timeframe": timeframe,

            "start": start,

            "end": end,

            "initial_balance": metrics.get("initial_balance"),

            "final_balance": metrics.get("final_balance"),

            "net_profit": metrics.get("net_profit"),

            "roi": metrics.get("roi"),

            "trade": metrics.get("trade"),

            "win": metrics.get("win"),

            "loss": metrics.get("loss"),

            "win_rate": metrics.get("win_rate"),

            "average_profit": metrics.get("average_profit"),

            "average_loss": metrics.get("average_loss"),

            "largest_win": metrics.get("largest_win"),

            "largest_loss": metrics.get("largest_loss"),

            "profit_factor": metrics.get("profit_factor"),

            "expectancy": metrics.get("expectancy"),

            "max_drawdown": metrics.get("max_drawdown"),

            "sharpe_ratio": metrics.get("sharpe_ratio"),

            "average_holding": metrics.get("average_holding"),

            "leverage": metrics.get("leverage"),
            
            "equity_curve":metrics.get("equity_curve"),
        }

        return report