from typing import Any, List

from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings

from app.config import settings
from app.core.vector_store_service import VectorStoreService


class ChromaService(VectorStoreService):
    def __init__(self, collection_name: str, embedding_function: Embeddings):
        self.embedding_function = embedding_function
        self.vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=self.embedding_function,
            persist_directory=settings.CHROMA_DB_PATH,
        )

    def add_items(self, items: List[Any]):
        self.vector_store.add_documents(
            documents=items,
            ids=[str(item.id) for item in items],
        )

    def query_items(self, query: str, n_results: int = 5) -> List[Any]:
        return self.vector_store.similarity_search(query, n_results)

    def delete_items(self, items: List[Any]):
        self.vector_store.delete_documents(
            documents=items,
            ids=[str(item.id) for item in items],
        )

    def update_items(self, items: List[Any]):
        self.vector_store.update_documents(
            documents=items,
            ids=[str(item.id) for item in items],
        )
