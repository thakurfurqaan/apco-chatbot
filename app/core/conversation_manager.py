from app.core.ai_client import AIClientInterface
from app.core.ecommerce_service import EcommerceServiceInterface


class ConversationManager:
    """Handles the conversation logic and coordinates between AI and E-commerce modules."""

    def __init__(
        self, ai_client: AIClientInterface, ecommerce_service: EcommerceServiceInterface
    ):
        self.ai_client = ai_client
        self.ecommerce_service = ecommerce_service

    def process_text_input(self, message: str) -> str:
        """
        Process a text input and generate a response.

        Args:
            message (str): The message to process.

        Returns:
            str: The response from the AI client.
        """
        response = self.ai_client.generate_response(message)
        return response
