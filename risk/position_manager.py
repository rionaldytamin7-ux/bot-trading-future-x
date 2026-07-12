class PositionManager:


    def __init__(

        self,

        leverage=10

    ):

        self.leverage = leverage



    def calculate(

        self,

        entry,

        stop_loss,

        risk_reward=2

    ):


        risk = abs(
            entry - stop_loss
        )


        take_profit = entry + (
            risk * risk_reward
        )


        return {


            "entry": entry,

            "stop_loss": stop_loss,

            "take_profit": take_profit,

            "leverage": self.leverage,

            "risk_reward": risk_reward

        }

class AutoCompound:

    def calculate_balance(self, wallet):

        return float(wallet)

    def next_position_size(
        self,
        wallet,
        risk_percent
    ):

        return wallet * (risk_percent / 100)