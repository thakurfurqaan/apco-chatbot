import traceback
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.ecommerce_service import get_ecommerce_service
from app.core.ecommerce_service import EcommerceServiceInterface
from app.schemas.ecommerce import ProductResponse
from app.services.ai_client.langchain.dependencies.embedding import (
    get_embedding_function,
)
from app.services.vector_store.chroma_service import ChromaVectorStore

router = APIRouter()


@router.post("/products/sync")
async def sync_products_vector_store(
    ecommerce_service: EcommerceServiceInterface = Depends(get_ecommerce_service),
):
    embedding_function = get_embedding_function()
    collection_name = "products"
    vector_store = ChromaVectorStore(
        collection_name=collection_name, embedding_function=embedding_function
    )
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
        print(e)
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/products", response_model=List[ProductResponse])
def get_products(
    ecommerce_service: EcommerceServiceInterface = Depends(get_ecommerce_service),
):
    return ecommerce_service.get_all_products()
