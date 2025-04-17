from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .config import DATABASE_URL


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class WalletRequest(Base):
    __tablename__ = 'wallet_requests'

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String, index=True)
    bandwidth = Column(Integer)
    energy = Column(Integer)
    balance = Column(String)
    timestamp = Column(DateTime, default=func.now())


Base.metadata.create_all(bind=engine)
