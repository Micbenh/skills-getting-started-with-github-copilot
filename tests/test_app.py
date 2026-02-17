from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_activity():
    response = client.post("/activities/Soccer/signup?email=test@example.com")
    assert response.status_code == 200 or response.status_code == 400
    assert "message" in response.json() or "detail" in response.json()

def test_unregister_activity():
    response = client.delete("/activities/Soccer/unregister?email=test@example.com")
    assert response.status_code == 200 or response.status_code == 400
    assert "message" in response.json() or "detail" in response.json()