from abc import ABC, abstractmethod
from typing import Any, List


class VectorStoreInterface(ABC):
    """Interface for a vector store."""

    @abstractmethod
    def add_items(self, ids: List[str], contents: List[str], metadatas: List[dict]):
        """Add items to the vector store."""
        pass

    @abstractmethod
    def query_items(self, query: str, n_results: int = 5) -> List[Any]:
        """Query the vector store."""
        pass

    @abstractmethod
    def delete_items(self, ids: List[str]):
        """Delete items from the vector store."""
        pass

    @abstractmethod
    def update_items(self, ids: List[str], contents: List[str], metadatas: List[dict]):
        """Update items in the vector store."""
        pass
