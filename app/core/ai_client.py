from abc import ABC, abstractmethod


class ContextConstructor(ABC):
    @abstractmethod
    def construct_context(self):
        pass


class RAGChainCreator(ABC):
    @abstractmethod
    def create_rag_chain(self):
        pass


class AIClientInterface(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass
