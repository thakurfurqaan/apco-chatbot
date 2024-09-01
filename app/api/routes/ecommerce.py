from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.containers import Container
from app.core.ecommerce_service import EcommerceServiceInterface
from app.core.vector_store import VectorStoreInterface
from app.schemas.ecommerce import ProductResponse

router = APIRouter()


@router.post("/products/sync")
@inject
async def sync_products_vector_store(
    ecommerce_service: EcommerceServiceInterface = Depends(
        Provide[Container.ecommerce_service]
    ),
    vector_store: VectorStoreInterface = Depends(
        Provide[Container.product_vector_store]
    ),
):
    products = ecommerce_service.get_all_products()
    try:
        vector_store.add_items(
            ids=[str(product.id) for product in products],
            contents=[product.description for product in products],
            metadatas=[
                {"name": product.name, "tags": ",".join(product.tags)}
                for product in products
            ],
        )
        return {"message": "Successfully updated products in the vector store"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/products", response_model=List[ProductResponse])
@inject
async def get_products(
    ecommerce_service: EcommerceServiceInterface = Depends(
        Provide[Container.ecommerce_service]
    ),
):
    return ecommerce_service.get_all_products()
