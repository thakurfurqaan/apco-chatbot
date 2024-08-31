from abc import ABC, abstractmethod
from typing import Any, List


class VectorStoreService(ABC):

    @abstractmethod
    def add_item(self, item: Any):
        pass

    @abstractmethod
    def query_items(self, query: str, n_results: int = 5) -> List[Any]:
        pass

    @abstractmethod
    def delete_item(self, item: Any):
        pass

    @abstractmethod
    def update_item(self, item: Any):
        pass
