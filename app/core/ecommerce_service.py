from abc import ABC, abstractmethod
from typing import List

from app.schemas.ecommerce import ProductBase


class EcommerceServiceInterface(ABC):
    """Interface for E-commerce service."""

    @abstractmethod
    def get_all_products(self) -> List[ProductBase]:
        pass
