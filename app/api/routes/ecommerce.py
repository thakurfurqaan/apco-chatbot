from fastapi import APIRouter

from app.schemas.ecommerce import ProductRequest, ProductResponse
from app.services.ecommerce.ecommerce_mock import EcommerceMock

router = APIRouter()


@router.post("/products/list", response_model=ProductResponse)
async def list_products(
    request: ProductRequest,
):
    response = EcommerceMock.list_products()
    return response
