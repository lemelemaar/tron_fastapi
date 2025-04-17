from pydantic import BaseModel
from datetime import datetime


class WalletRequestCreate(BaseModel):
    wallet_address: str


class WalletRequestResponse(BaseModel):
    id: int
    wallet_address: str
    bandwidth: int
    energy: int
    balance: str
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }
