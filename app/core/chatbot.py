from abc import ABC, abstractmethod


class ChatbotInterface(ABC):
    """AI-powered chatbot."""

    @abstractmethod
    def query(self, query: str):
        pass

    @abstractmethod
    def format_response(self, response: str):
        pass
