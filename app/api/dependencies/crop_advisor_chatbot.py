from app.api.dependencies.ecommerce_service import get_ecommerce_service
from app.core.chatbot import ChatbotInterface
from app.core.conversation_manager import ConversationManager
from app.services.ai_client.langchain.client import LangChainClient
from app.services.ai_client.langchain.dependencies.embedding import (
    get_embedding_function,
)
from app.services.chatbot.crop_advisor_chatbot import CropAdvisorChatbot
from app.services.vector_store.chroma_service import ChromaVectorStore


def get_crop_advisor_chatbot() -> ChatbotInterface:
    embedding_function = get_embedding_function()
    vector_store = ChromaVectorStore(
        collection_name="products", embedding_function=embedding_function
    )
    ai_client = LangChainClient(vector_store=vector_store)
    ecommerce_service = get_ecommerce_service()
    conversation_manager = ConversationManager(
        ai_client=ai_client, ecommerce_service=ecommerce_service
    )

    return CropAdvisorChatbot(conversation_manager)
