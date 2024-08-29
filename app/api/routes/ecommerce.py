from typing import List

from fastapi import APIRouter, Depends

from app.api.dependencies import get_ecommerce_service
from app.core.ecommerce_service import EcommerceService
from app.schemas.ecommerce import ProductResponse

router = APIRouter()


@router.get("/products", response_model=List[ProductResponse])
async def get_products(
    ecommerce_service: EcommerceService = Depends(get_ecommerce_service),
):
    products = await ecommerce_service.get_all_products()
    return [ProductResponse.from_orm(product) for product in products]
