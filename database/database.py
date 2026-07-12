from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "sqlite:///rio.db"

from config import Config

engine = create_engine(
    Config.DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(
    bind=engine
)


def init_database():
    from database.models import Base
    Base.metadata.create_all(bind=engine)