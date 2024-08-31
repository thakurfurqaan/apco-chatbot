from app.core.chatbot_service import ChatbotService
from app.core.ecommerce_service import EcommerceService


class ConversationManager:
    """Handles the conversation logic and coordinates between AI and E-commerce modules."""

    def __init__(
        self, chatbot_service: ChatbotService, ecommerce_service: EcommerceService
    ):
        self.chatbot_service = chatbot_service
        self.ecommerce_service = ecommerce_service

    def send_message(self, message: str) -> str:
        product_data = self.ecommerce_service.get_all_products()
        response = self.chatbot_service.query(message)
        return self._format_response(response)

    def _format_response(self, response: str) -> str:
        return response.strip().replace("*", "")
