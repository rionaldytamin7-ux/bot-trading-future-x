from database.trade_repository import TradeRepository


class Statistics:


    def __init__(self):

        self.repo = TradeRepository()



    def get_summary(self):


        trades = self.repo.get_all()


        total = len(trades)


        if total == 0:

            return {

                "trade":0,

                "win_rate":0

            }


        win = len(
            [
                t for t in trades
                if t.win
            ]
        )


        win_rate = (
            win / total
        ) * 100



        return {


            "trade": total,


            "win": win,


            "loss": total-win,


            "win_rate": round(
                win_rate,
                2
            )


        }
    
    def live_dashboard(self):

        return {

            "balance": self.balance,

            "floating": self.floating,

            "today_profit": self.today_profit,

            "today_trade": self.today_trade,

            "win_rate": self.win_rate,

            "open_position": self.open_position

        }
    
    