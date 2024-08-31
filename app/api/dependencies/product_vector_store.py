from app.core.vector_store import VectorStoreInterface
from app.services.ai_client.langchain.dependencies.embedding import (
    get_embedding_function,
)
from app.services.vector_store.chroma_service import ChromaVectorStore


def get_product_vector_store(
    collection_name: str, embedding_function
) -> VectorStoreInterface:
    collection_name = "products"
    embedding_function = get_embedding_function()
    return ChromaVectorStore(
        collection_name=collection_name, embedding_function=embedding_function
    )
