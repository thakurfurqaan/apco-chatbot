from abc import ABC, abstractmethod


class ContextConstructor(ABC):
    @abstractmethod
    def construct_context(self):
        """
        Construct the context for the AI client.

        Returns:
            str: The context for the AI client.
        """
        pass


class RAGChainCreator(ABC):
    @abstractmethod
    def create_rag_chain(self):
        """
        Create a RAG chain for the AI client.

        Returns:
            str: The RAG chain for the AI client.
        """
        pass


class AIClientInterface(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the AI client.

        Args:
            prompt (str): The prompt to generate a response for.

        Returns:
            str: The response from the AI client.
        """
        pass
