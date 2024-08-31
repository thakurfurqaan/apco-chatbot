from abc import ABC, abstractmethod


class ChatbotInterface(ABC):
    """AI-powered chatbot."""

    @abstractmethod
    def send_message(self, message: str) -> str:
        pass

    @abstractmethod
    def format_response(self, response: str) -> str:
        pass
