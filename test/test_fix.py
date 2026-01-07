from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_valid_value_returns_result():
    response = client.post("/process", json={"value": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 10}


def test_negative_value_returns_400():
    response = client.post("/process", json={"value": -3})
    assert response.status_code == 400
