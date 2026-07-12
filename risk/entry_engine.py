class EntryEngine:


    def __init__(

        self,

        leverage=10

    ):

        self.leverage = leverage



    def calculate(

        self,

        symbol,

        side,

        price,

        support,

        resistance,

        risk_reward=2

    ):



        entry = price



        # =====================
        # LONG SETUP
        # =====================

        if side == "LONG":


            stop_loss = support


            risk = entry - stop_loss


            take_profit = (

                entry +

                (risk * risk_reward)

            )



        # =====================
        # SHORT SETUP
        # =====================

        elif side == "SHORT":


            stop_loss = resistance


            risk = stop_loss - entry


            take_profit = (

                entry -

                (risk * risk_reward)

            )



        else:


            return None



        return {


            "symbol": symbol,


            "side": side,


            "entry": round(
                entry,
                2
            ),


            "stop_loss": round(
                stop_loss,
                2
            ),


            "take_profit": round(
                take_profit,
                2
            ),


            "risk_reward": risk_reward,


            "leverage": self.leverage

        }