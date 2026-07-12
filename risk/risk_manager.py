"""
RIO AI FUTURES
Risk Management
"""


from config import Config



class RiskManager:


    def __init__(self):

        self.risk = Config.DEFAULT_RISK



    def calculate_position_size(

            self,

            balance,

            price,

            stop_loss_percent=0.02

    ):


        risk_amount = balance * self.risk


        stop_distance = price * stop_loss_percent


        quantity = risk_amount / stop_distance


        return quantity



    def calculate_stop_loss(

            self,

            entry,

            percent=0.02

    ):


        return entry - (

            entry * percent

        )



    def calculate_take_profit(

            self,

            entry,

            percent=0.04

    ):


        return entry + (

            entry * percent

        )