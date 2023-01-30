from fastapi.testclient import TestClient

from backlog_tracker.app import app
from backlog_tracker.db.session import get_db
from tests.conftest import db_session

app.dependency_overrides[get_db] = db_session

client = TestClient(app)


# TODO: Rewrite on classes
def test_create_user():
    response = client.post(
        "/users/",
        json={
            'username': 'deadpool',
            'password': 'verysecretpassword',
            'email': 'deadpool@example.com'
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert "id" in data

    user_id = data["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    assert data["id"] == user_id
