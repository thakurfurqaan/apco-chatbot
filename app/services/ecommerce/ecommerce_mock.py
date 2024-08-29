from typing import List

from app.core.ecommerce_service import EcommerceService
from app.schemas.ecommerce import Product


class EcommerceMock(EcommerceService):
    async def get_all_products(self) -> List[Product]:
        return [
            Product(
                name="Product 1",
                description="Description 1",
                price=10.0,
                image="https://example.com/image1.jpg",
            )
        ]
