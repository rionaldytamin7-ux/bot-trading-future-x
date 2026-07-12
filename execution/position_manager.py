from datetime import datetime



class PositionManager:


    def __init__(self):

        self.position = None



    def open_position(self, trade):


        self.position = {


            "symbol":
            trade["symbol"],


            "side":
            trade["side"],


            "entry":
            trade["entry"],


            "stop_loss":
            trade["stop_loss"],


            "take_profit":
            trade["take_profit"],


            "leverage":
            trade["leverage"],


            "opened_at":
            datetime.utcnow()

        }


        return self.position



    def check_position(self, price):


        if self.position is None:

            return None



        side = self.position["side"]



        # LONG

        if side == "LONG":


            if price >= self.position["take_profit"]:


                return self.close_position(
                    price,
                    "TP"
                )



            elif price <= self.position["stop_loss"]:


                return self.close_position(
                    price,
                    "SL"
                )



        # SHORT

        elif side == "SHORT":


            if price <= self.position["take_profit"]:


                return self.close_position(
                    price,
                    "TP"
                )



            elif price >= self.position["stop_loss"]:


                return self.close_position(
                    price,
                    "SL"
                )



        return {

            "status":
            "HOLD"

        }



    def close_position(

        self,

        exit_price,

        reason

    ):


        entry = self.position["entry"]

        side = self.position["side"]



        if side == "LONG":

            pnl = (
                exit_price-entry
            )


        else:

            pnl = (
                entry-exit_price
            )



        result = {


            "symbol":
            self.position["symbol"],


            "side":
            side,


            "entry":
            entry,


            "exit":
            exit_price,


            "pnl":
            round(
                pnl,
                2
            ),


            "reason":
            reason


        }


        self.position = None


        return result
    
    def floating_pnl(self, symbol):

        position = self.get_position(symbol)

        if position is None:
            return 0

        return float(position["unRealizedProfit"])

    def is_open(self, symbol):

        position = self.get_position(symbol)

        if position is None:
            return False

        return abs(float(position["positionAmt"])) > 0

    def check_exit(self, symbol):

        position = self.get_position(symbol)

        if position is None:
            return "CLOSED"

        qty = abs(float(position["positionAmt"]))

        if qty == 0:
            return "CLOSED"

        return "OPEN"
    

class PositionSizing:

    def __init__(self, risk_percent=1):
        self.risk_percent = risk_percent

    def calculate(
        self,
        balance,
        entry_price,
        stop_loss,
        leverage=10
    ):

        risk_money = balance * (self.risk_percent / 100)

        stop_distance = abs(entry_price - stop_loss)

        if stop_distance == 0:
            return 0

        quantity = (
            risk_money /
            stop_distance
        ) * leverage

        return round(quantity, 6)

#QUANTITY SIZING BALANCE
        qty = sizing.calculate(
            wallet = account.get_balance()
            balance = compound.calculate_balance(
                wallet
            ),
            entry_price=62000,
            stop_loss=61800,
            leverage=10
        )
#soon
# sizing = PositionSizing(
#     risk_percent=1
# )

