from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_chat_endpoint_text_only():
    response = client.post(
        "/chat",
        data={
            "message": "I need a product to control fungal diseases in my wheat crop"
        },
    )
    assert response.status_code == 200
    assert "message" in response.json()


def test_chat_endpoint_text_and_file():
    with open("tests/test-crop-disease-image.webp", "rb") as file:
        files = {"file": ("test-crop-disease-image.webp", file, "image/webp")}
        data = {
            "message": "I need a product to control fungal diseases in my wheat crop"
        }

        response = client.post("/chat", data=data, files=files)

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
