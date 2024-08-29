from app.core.ai_service import AIService
from app.core.ecommerce_service import EcommerceService


class ConversationManager:
    def __init__(self, ai_service: AIService, ecommerce_service: EcommerceService):
        self.ai_service = ai_service
        self.ecommerce_service = ecommerce_service

    async def send_message(self, message: str) -> str:
        product_data = await self.ecommerce_service.get_all_products()
        response = await self.ai_service.process_prompt(
            f"{message}\nProduct data: {product_data}"
        )
        return self._format_response(response)

    def _format_response(self, response: str) -> str:
        return response.strip().replace("*", "")
