from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_student():
    response = client.post(
        "/students/",
        json={"name": "John", "age": 25, "address": {"city": "New York", "country": "USA"}}
    )
    assert response.status_code == 201
    assert "id" in response.json()
