from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal
from .config import client
from typing import List


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/wallet", response_model=schemas.WalletRequestResponse)
def fetch_wallet_info(request: schemas.WalletRequestCreate, db: Session = Depends(get_db)):
    wallet_address = request.wallet_address

    try:
        balance = client.get_account_balance(wallet_address)

        resource = client.get_account_resource(wallet_address)

        free_net_limit = resource.get("freeNetLimit", 0)
        free_net_used = resource.get("freeNetUsed", 0)
        net_limit = resource.get("NetLimit", 0)
        net_used = resource.get("NetUsed", 0)
        bandwidth = (free_net_limit - free_net_used) + (net_limit - net_used)

        energy_limit = resource.get("EnergyLimit", 0)
        energy_used = resource.get("EnergyUsed", 0)
        energy = energy_limit - energy_used

        wallet_request = crud.create_wallet_request(
            db,
            wallet_address=wallet_address,
            bandwidth=bandwidth,
            energy=energy,
            balance=str(balance)
        )

        return wallet_request

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/wallets", response_model=List[schemas.WalletRequestResponse])
def get_wallets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_wallet_requests(db, skip=skip, limit=limit)
