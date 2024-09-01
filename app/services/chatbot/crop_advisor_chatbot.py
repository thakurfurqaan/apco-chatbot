from app.core.chatbot import ChatbotInterface
from app.core.conversation_manager import ConversationManager


class CropAdvisorChatbot(ChatbotInterface):
    """AI-powered chatbot for diagnosing and treating crop diseases and suggesting relevant products."""

    def __init__(self, conversation_manager: ConversationManager):
        self.conversation_manager: ConversationManager = conversation_manager

    def send_message(self, message: str):
        """
        Send a message to the chatbot and get a response.

        Args:
            message (str): The message to send to the chatbot.

        Returns:
            str: The response from the chatbot.
        """
        response = self.conversation_manager.process_text_input(message)
        return self.format_response(response)

    def format_response(self, response: str):
        """
        Format the response from the chatbot.

        Args:
            response (str): The response from the chatbot.

        Returns:
            str: The formatted response.
        """
        return response
