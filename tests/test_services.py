from app.services.ecommerce.ecommerce_mock.ecommerce_mock import EcommerceMockService


def test_ecommerce_service():
    service = EcommerceMockService()
    products = service.get_all_products()
    assert isinstance(products, list)
