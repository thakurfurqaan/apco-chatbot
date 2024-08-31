from app.core.ecommerce_service import EcommerceServiceInterface
from app.services.ecommerce.ecommerce_mock.ecommerce_mock import EcommerceMockService


def get_ecommerce_service() -> EcommerceServiceInterface:
    ecommerce_service = EcommerceMockService()
    return ecommerce_service
