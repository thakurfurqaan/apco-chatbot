from app.core.ai_service import AIService
from app.core.chatbot_service import ChatbotService


class CropAdvisorChatbot(ChatbotService):
    """AI-powered chatbot for diagnosing and treating crop diseases and suggesting relevant products."""

    def __init__(self, ai_service: AIService):
        self.ai_service: AIService = ai_service

    def query(self, query: str):
        return self.ai_service.process_prompt(query)
