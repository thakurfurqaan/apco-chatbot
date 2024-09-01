from typing import Any, List

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

from app.core.vector_store import VectorStoreInterface


class ChromaVectorStore(VectorStoreInterface):
    def __init__(
        self,
        collection_name: str,
        embedding_function: Embeddings,
        persist_directory: str,
    ):
        self._embedding_function = embedding_function
        self._vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=self._embedding_function,
            persist_directory=persist_directory,
        )

    def add_items(self, ids: List[str], contents: List[str], metadatas: List[dict]):
        self._vector_store.add_documents(
            documents=self._create_documents(ids, contents, metadatas), ids=ids
        )

    def _create_documents(
        self, ids: List[str], contents: List[str], metadatas: List[dict]
    ):
        documents = []

        for id, content, metadata in zip(ids, contents, metadatas):
            document = Document(page_content=content, metadata=metadata, id=id)
            documents.append(document)
        return documents

    def query_items(self, query: str, n_results: int = 5) -> List[Any]:
        return self._vector_store.similarity_search(query, n_results)

    def delete_items(self, ids: List[str]):
        self._vector_store.delete(ids=ids)

    def update_items(self, ids: List[str], contents: List[str], metadatas: List[dict]):
        self._vector_store.update_documents(
            documents=self._create_documents(ids, contents, metadatas),
            ids=ids,
        )
