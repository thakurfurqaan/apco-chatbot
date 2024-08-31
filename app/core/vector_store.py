from abc import ABC, abstractmethod
from typing import Any, List


class VectorStoreInterface(ABC):

    @abstractmethod
    def add_items(self, ids: List[str], contents: List[str], metadatas: List[dict]):
        pass

    @abstractmethod
    def query_items(self, query: str, n_results: int = 5) -> List[Any]:
        pass

    @abstractmethod
    def delete_items(self, ids: List[str]):
        pass

    @abstractmethod
    def update_items(self, ids: List[str], contents: List[str], metadatas: List[dict]):
        pass
