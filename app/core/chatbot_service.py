from abc import ABC, abstractmethod


class ChatbotService(ABC):
    """AI-powered chatbot."""

    @abstractmethod
    def query(self, query: str):
        pass
