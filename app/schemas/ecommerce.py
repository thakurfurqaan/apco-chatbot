from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: str
    name: str
    description: str
    tags: List[str]


class Product(ProductBase):
    pass


class ProductResponse(ProductBase):
    pass
