from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat_endpoint():
    response = client.post(
        "/chat",
        json={
            "message": "I need a product to control fungal diseases in my wheat crop"
        },
    )
    assert response.status_code == 200
    assert "message" in response.json()


def test_products_endpoint():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_product_sync_endpoint():
    response = client.post("/products/sync")
    assert response.status_code == 200
    assert "message" in response.json()
    assert (
        response.json()["message"]
        == "Successfully updated products in the vector store"
    )
