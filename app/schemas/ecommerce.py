from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: str
    name: str
    description: str
    tags: List[str]


class ProductResponse(ProductBase):
    pass
