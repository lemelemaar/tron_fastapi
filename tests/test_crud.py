import pytest
from app import crud
from app.database import Base, engine, SessionLocal


@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


def test_create_wallet_request(db):
    wallet = crud.create_wallet_request(
        db,
        wallet_address="TTest123456",
        bandwidth=99,
        energy=5,
        balance="123.456789"
    )

    assert wallet.id is not None
    assert wallet.wallet_address == "TTest123456"
    assert wallet.bandwidth == 99
    assert wallet.energy == 5
    assert wallet.balance == "123.456789"
