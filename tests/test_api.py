from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat_endpoint():
    response = client.post("/chat", json={"message": "Hello, chatbot!"})
    assert response.status_code == 200
    assert "message" in response.json()


def test_products_endpoint():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
