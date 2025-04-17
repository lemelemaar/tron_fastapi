from sqlalchemy.orm import Session
from . import database


def create_wallet_request(db: Session, wallet_address: str, bandwidth: int, energy: int, balance: str):
    db_wallet_request = database.WalletRequest(
        wallet_address=wallet_address,
        bandwidth=bandwidth,
        energy=energy,
        balance=balance,
    )
    db.add(db_wallet_request)
    db.commit()
    db.refresh(db_wallet_request)
    return db_wallet_request


def get_wallet_requests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(database.WalletRequest).offset(skip).limit(limit).all()
