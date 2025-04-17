import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine


client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_post_and_get_wallet():
    address = "TPtSojdZmxzZfzxf9fpLXErmr5QPDzymWd"

    # POST
    response = client.post("/wallet", json={"wallet_address": address})
    assert response.status_code == 200
    data = response.json()
    assert data["wallet_address"] == address
    assert "bandwidth" in data
    assert "energy" in data
    assert "balance" in data

    # GET
    response = client.get("/wallets")
    assert response.status_code == 200
    data = response.json()
    assert any(wallet["wallet_address"] == address for wallet in data)
