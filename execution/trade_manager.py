from database.trade_repository import TradeRepository
from ai.dataset import DatasetBuilder
dataset = DatasetBuilder()


class TradeManager:

    trade["quantity"] = filter.normalize_quantity(
        trade["symbol"],
        trade["quantity"]
    )

    trade["entry"] = filter.normalize_price(
        trade["symbol"],
        trade["entry"]
    )

    trade["stop_loss"] = filter.normalize_price(
        trade["symbol"],
        trade["stop_loss"]
    )

    trade["take_profit"] = filter.normalize_price(
        trade["symbol"],
        trade["take_profit"]
    )

    def __init__(self):

        self.repo = TradeRepository()



    def save_open_trade(

        self,

        trade

    ):


        data = {


            "symbol":
            trade["symbol"],


            "side":
            trade["side"],


            "entry_price":
            trade["entry"],


            "stop_loss":
            trade["stop_loss"],


            "take_profit":
            trade["take_profit"],


            "leverage":
            trade["leverage"],


            "status":
            "OPEN"


        }


        return self.repo.create_trade(
            data
        )



    def close_trade(

        self,

        trade_id,

        result

    ):


        return self.repo.close_trade(

            trade_id,

            result

        )
    
    def place_protection_orders(self, trade):

        side = "SELL" if trade["side"] == "BUY" else "BUY"

        # Stop Loss
        sl_order = self.client.futures_create_order(
            symbol=trade["symbol"],
            side=side,
            type="STOP_MARKET",
            stopPrice=trade["stop_loss"],
            closePosition=True
        )

        if order is None:

            logger.error(
                "Order Failed"
            )

            return False

        logger.info(
            f"Order ID : {order['orderId']}"
        )

        logger.info(
            f"Status   : {order['status']}"
        )

        # Take Profit
        tp_order = self.client.futures_create_order(
            symbol=trade["symbol"],
            side=side,
            type="TAKE_PROFIT_MARKET",
            stopPrice=trade["take_profit"],
            closePosition=True
        )

        if order is None:

            logger.error(
                "Order Failed"
            )

            return False

        logger.info(
            f"Order ID : {order['orderId']}"
        )

        logger.info(
            f"Status   : {order['status']}"
        )

        return {
            "sl": sl_order,
            "tp": tp_order
        }
    
#ORDER INFO
        order_info = client.futures_get_order(

            symbol=trade["symbol"],

            orderId=order["orderId"]

        )

        if order_info["status"] != "FILLED":

            logger.warning(
                "Waiting Filled..."
            )

            return
        
#Simpan Average Entry
        trade["entry"] = float(
            order_info["avgPrice"]
        )
#HITUNG REAL QUANTITY
        trade["quantity"] = float(

            order_info["executedQty"]

        )
#VERIF POSISI
        position = client.futures_position_information(

            symbol=trade["symbol"]

        )

        float(position[0]["positionAmt"]) == 0

        logger.error(
            "Position Not Found"
        )

    def move_stop_to_break_even(self, trade):

        trade["stop_loss"] = trade["entry"]

        trade["break_even"] = True

        return trade

    def enable_trailing_stop(self, trade):

        trade["trailing_stop"] = True

        return trade

    def partial_close(self, trade, percent):

        quantity = trade["quantity"] * (percent / 100)

        return quantity
    


#save database
protection = self.place_protection_orders(
    trade
)


dataset.append({

    "symbol": trade.symbol,

    "timeframe": trade.timeframe,

    "side": trade.side,

    "entry": trade.entry_price,

    "exit": trade.exit_price,

    "stop_loss": trade.stop_loss,

    "take_profit": trade.take_profit,

    "risk_reward": trade.risk_reward,

    "leverage": trade.leverage,

    "quantity": trade.quantity,

    "ai_score": trade.ai_score,

    "market_regime": trade.market_regime,

    "pattern": trade.pattern,

    "volume_status": trade.volume_status,

    "btc_dominance": trade.btc_dominance,

    "funding_rate": trade.funding_rate,

    "result": trade.result,

    "pnl": trade.pnl,

    "win": trade.win

})


trade = {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "entry": 62000,
    "stop_loss": 61600,

    "tp1": 62400,
    "tp2": 62800,
    "tp3": 63500,

    "tp1_percent": 30,
    "tp2_percent": 30,
    "tp3_percent": 40,

    "break_even": False,

    "trailing_stop": False,

    "quantity": qty,

    "leverage": 10
}

trade["status"] = "FILLED"

repository.update_trade(trade)

trade["status"] = "TP1"

repository.update_trade(trade)

trade["status"] = "TP2"

repository.update_trade(trade)

trade["status"] = "CLOSED"

repository.update_trade(trade)

trade["status"] = "STOP_LOSS"

repository.update_trade(trade)