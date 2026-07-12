from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Base(DeclarativeBase):
    pass


class Trade(Base):

    __tablename__ = "trades"

    id = Column(Integer, primary_key=True)

    symbol = Column(String)

    side = Column(String)

    entry_price = Column(Float)

    exit_price = Column(
    Float,
    nullable=True
    )

    stop_loss = Column(Float
    )

    take_profit = Column(Float
    )

    leverage = Column(Integer)

    margin = Column(Float)

    quantity = Column(Float)

    pnl = Column(Float, default=0)

    pnl_percent = Column(Float, default=0)
    win = Column(
        Boolean,
        default=False)
    ai_score = Column(Float)

    strategy = Column(
        String)

    status = Column(
        String,
        default="OPEN")

    created_at = Column(
        DateTime,
        default=datetime.utcnow)

    closed_at = Column(
        DateTime,
        nullable=True)