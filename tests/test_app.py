from fastapi.testclient import TestClient
from backlog_tracker.app import app

client = TestClient(app)


def test_ping():
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to Backlog Tracker' in response.content
