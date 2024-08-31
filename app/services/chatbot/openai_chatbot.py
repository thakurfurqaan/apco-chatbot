from app.core.chatbot_service import ChatbotInterface
from app.core.conversation_manager import ConversationManager


class CropAdvisorChatbot(ChatbotInterface):
    """AI-powered chatbot for diagnosing and treating crop diseases and suggesting relevant products."""

    def __init__(self, conversation_manager: ConversationManager):
        self.conversation_manager: ConversationManager = conversation_manager

    def query(self, query: str):
        response = self.conversation_manager.process_text_input(query)
        return self.format_response(response)

    def format_response(self, response: str):
        return response
