from typing import Any, List

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from app.config import settings
from app.core.vector_store_service import VectorStoreService


class ChromaService(VectorStoreService):
    def __init__(self, collection_name: str):
        self.embedding_function = OpenAIEmbeddings(
            api_key=settings.OPENAI_API_KEY, model_name=settings.OPENAI_EMBEDDING_MODEL
        )
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
