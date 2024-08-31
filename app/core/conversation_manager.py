from app.core.ai_service import AIClientInterface
from app.core.ecommerce_service import EcommerceServiceInterface


class ConversationManager:
    """Handles the conversation logic and coordinates between AI and E-commerce modules."""

    def __init__(
        self, ai_client: AIClientInterface, ecommerce_service: EcommerceServiceInterface
    ):
        self.ai_client = ai_client
        self.ecommerce_service = ecommerce_service

    def process_text_input(self, message: str) -> str:
        response = self.ai_client.generate_response(message)
        return self._format_response(response)

    def _format_response(self, response: str) -> str:
        return response.strip().replace("*", "")
