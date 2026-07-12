from database.database import SessionLocal
from database.models import Trade


from datetime import datetime

class TradeRepository:


    def create_trade(
        self,
        data
    ):

        db = SessionLocal()


        trade = Trade(**data)


        db.add(trade)

        db.commit()

        db.refresh(trade)

        db.close()


        return trade



    def get_all(self):

        db = SessionLocal()


        trades = db.query(
            Trade
        ).all()


        db.close()


        return trades



    def count_win(self):

        db = SessionLocal()


        result = db.query(
            Trade
        ).filter(
            Trade.win == True
        ).count()

        db.close()
        return result
    
    def close_trade(
        self,
        trade_id,
        result):

        db = SessionLocal()

        trade = db.query(
            Trade
        ).filter(
            Trade.id == trade_id
        ).first()

        if trade:
            trade.exit_price = result["exit"]

            trade.pnl = result["pnl"]

            trade.status = "CLOSED"

            trade.closed_at = datetime.utcnow()

            if result["pnl"] > 0:

                trade.win = True

            else:

                trade.win = False

            db.commit()
        db.close()

        return trade
    
    
    def get_open_trade(self):

        return (

            self.session.query(Trade)

            .filter(

                Trade.status.in_(

                    [

                        "OPEN",

                        "TP1",

                        "TP2"

                    ]

                )

            )

            .all()

        )


TRADE_STATUS = {

    "NEW": "NEW",

    "FILLED": "FILLED",

    "OPEN": "OPEN",

    "TP1": "TP1",

    "TP2": "TP2",

    "TP3": "TP3",

    "STOP_LOSS": "STOP_LOSS",

    "CLOSED": "CLOSED",

    "CANCELLED": "CANCELLED"

}