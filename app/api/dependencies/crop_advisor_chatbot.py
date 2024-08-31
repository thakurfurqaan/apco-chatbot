from langchain_chroma import Chroma

from app.api.dependencies.ecommerce_service import get_ecommerce_service
from app.api.dependencies.product_vector_store import (
    get_product_vector_store_collection_name,
    get_product_vector_store_embedding_function,
)
from app.core.ai_client import AIClientInterface
from app.core.chatbot import ChatbotInterface
from app.core.conversation_manager import ConversationManager
from app.core.ecommerce_service import EcommerceServiceInterface
from app.services.ai_client.langchain.client import LangChainClientBuilder
from app.services.chatbot.crop_advisor_chatbot import CropAdvisorChatbot


def get_conversation_manager(
    ai_client: AIClientInterface, ecommerce_service: EcommerceServiceInterface
) -> ConversationManager:
    return ConversationManager(ai_client=ai_client, ecommerce_service=ecommerce_service)


def get_products_retriever():
    chroma_db = Chroma(
        collection_name=get_product_vector_store_collection_name(),
        embedding_function=get_product_vector_store_embedding_function(),
    )
    return chroma_db.as_retriever()


def get_ai_client() -> AIClientInterface:
    retriever = get_products_retriever()
    client = LangChainClientBuilder().with_retriever(retriever).build()
    return client


def get_crop_advisor_chatbot() -> ChatbotInterface:
    ai_client = get_ai_client()
    ecommerce_service = get_ecommerce_service()
    conversation_manager = get_conversation_manager(ai_client, ecommerce_service)
    return CropAdvisorChatbot(conversation_manager)
