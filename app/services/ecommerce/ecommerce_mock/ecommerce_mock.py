from typing import List

from app.core.ecommerce_service import EcommerceServiceInterface
from app.schemas.ecommerce import Product
from app.services.ecommerce.ecommerce_mock import products_data_mock


class EcommerceMockService(EcommerceServiceInterface):
    """Mock implementation of EcommerceService for testing."""

    def get_all_products(self) -> List[Product]:
        """
        Get all products.

        Returns:
            List[Product]: The list of products.
        """
        return [Product(**product) for product in products_data_mock.get_all_products()]
