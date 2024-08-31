from chromadb import PersistentClient
from chromadb.utils import embedding_functions

from app.config import settings
from app.core.vector_store_service import VectorStoreService


class ChromaService(VectorStoreService):
    def __init__(self, collection_name: str):
        self.client = PersistentClient(path=settings.CHROMA_DB_PATH)
        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=settings.OPENAI_API_KEY, model_name=settings.OPENAI_EMBEDDING_MODEL
        )
        self.collection = self.client.get_or_create_collection(
            name=collection_name, embedding_function=self.embedding_function
        )

    def add_item(self, item_id: str, item_metadata: dict, item_embedding: list):
        self.collection.add(
            ids=[str(item_id)],
            metadatas=[item_metadata],
            documents=[item_embedding],
        )

    def query_items(self, query: str, n_results: int = 5):
        results = self.collection.query(query_texts=[query], n_results=n_results)
        return results
