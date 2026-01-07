from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_bug_invalid_zero_value():
    response = client.post("/process", json={"value": 0})
    assert response.status_code == 400
