from abc import ABC, abstractmethod


class ChatbotInterface(ABC):
    """AI-powered chatbot."""

    @abstractmethod
    def send_message(self, message: str) -> str:
        """
        Send a message to the chatbot and get a response.

        Args:
            message (str): The message to send to the chatbot.

        Returns:
            str: The response from the chatbot.
        """
        pass

    @abstractmethod
    def format_response(self, response: str) -> str:
        """
        Format the response from the chatbot.

        Args:
            response (str): The response from the chatbot.

        Returns:
            str: The formatted response.
        """
        pass
