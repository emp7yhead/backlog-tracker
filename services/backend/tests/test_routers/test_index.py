from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_ping():
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Backlog Tracker' in response.content
