from pydantic import BaseModel


class ProductResponse(BaseModel):
    name: str
    description: str
    price: float
    image: str


class ProductRequest(BaseModel):
    pass


class Product(BaseModel):
    name: str
    description: str
    price: float
    image: str
