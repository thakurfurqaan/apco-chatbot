from typing import Any, List

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

from app.core.vector_store import VectorStoreInterface


class ChromaVS(VectorStoreInterface):
    def __init__(
        self,
        collection_name: str,
        embedding_function: embedding_functions.EmbeddingFunction,
        persist_directory: str,
    ):
        self._client = chromadb.Client(Settings(persist_directory=persist_directory))
        self._collection = self._client.get_or_create_collection(
            name=collection_name, embedding_function=embedding_function
        )

    def add_items(self, ids: List[str], contents: List[str], metadatas: List[dict]):
        self._collection.add(documents=contents, metadatas=metadatas, ids=ids)

    def query_items(self, query: str, n_results: int = 5) -> List[Any]:
        return self._collection.query(query_texts=[query], n_results=n_results)

    def delete_items(self, ids: List[str]):
        self._collection.delete(ids=ids)

    def update_items(self, ids: List[str], contents: List[str], metadatas: List[dict]):
        self._collection.update(
            documents=contents,
            metadatas=metadatas,
            ids=ids,
        )
