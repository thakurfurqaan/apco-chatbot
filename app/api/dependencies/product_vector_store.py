from app.core.vector_store import VectorStoreInterface
from app.services.ai_client.langchain.dependencies.embedding import (
    get_embedding_function,
)
from app.services.vector_store.chroma_vector_store import ChromaVectorStore

PRODUCT_VECTOR_STORE_COLLECTION_NAME = "products"


def get_product_vector_store_collection_name():
    return PRODUCT_VECTOR_STORE_COLLECTION_NAME


def get_product_vector_store_embedding_function():
    return get_embedding_function()


def get_product_vector_store() -> VectorStoreInterface:
    return ChromaVectorStore(
        collection_name=get_product_vector_store_collection_name(),
        embedding_function=get_product_vector_store_embedding_function(),
    )
