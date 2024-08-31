from typing import List

from app.core.ecommerce_service import EcommerceServiceInterface
from app.schemas.ecommerce import ProductBase
from app.services.ecommerce.ecommerce_mock import products_data_mock


class EcommerceMockService(EcommerceServiceInterface):
    """Mock implementation of EcommerceService for testing."""

    def get_all_products(self) -> List[ProductBase]:
        return products_data_mock.get_all_products()
