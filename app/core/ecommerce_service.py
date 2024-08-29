from abc import ABC, abstractmethod
from typing import List

from app.models.ecommerce import Product


class EcommerceService(ABC):
    @abstractmethod
    async def get_all_products(self) -> List[Product]:
        pass
