from abc import ABC, abstractmethod
from typing import List

from app.models.ecommerce import Product


class EcommerceService(ABC):
    @abstractmethod
    def get_all_products(self) -> List[Product]:
        pass
