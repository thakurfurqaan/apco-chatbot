from typing import List

from app.core.ecommerce_service import EcommerceService
from app.models.ecommerce import Product
from app.schemas.ecommerce import ProductResponse


class EcommerceMockService(EcommerceService):
    async def get_all_products(self) -> List[ProductResponse]:
        return [
            Product(
                name="Product 1",
                description="Description 1",
                price=10.0,
                image="https://example.com/image1.jpg",
            )
        ]
