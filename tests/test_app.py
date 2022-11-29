from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ping():
    response = client.get('/')
    assert response.status_code == 200
    assert response.content == b'Welcome to Backlog Tracker'
