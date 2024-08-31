from typing import List

from app.core.ecommerce_service import EcommerceService
from app.models.ecommerce import Product
from app.services.ecommerce.ecommerce_mock import products_data_mock


class EcommerceMockService(EcommerceService):
    def get_all_products(self) -> List[Product]:
        return products_data_mock.get_all_products()
