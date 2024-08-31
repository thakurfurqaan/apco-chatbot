from app.api.dependencies.ecommerce_service import get_ecommerce_service
from app.core.ai_client import AIClientInterface
from app.core.chatbot import ChatbotInterface
from app.core.conversation_manager import ConversationManager
from app.core.ecommerce_service import EcommerceServiceInterface
from app.core.vector_store import VectorStoreInterface
from app.services.ai_client.langchain.client import LangChainClientBuilder
from app.services.ai_client.langchain.dependencies.embedding import (
    get_embedding_function,
)
from app.services.chatbot.crop_advisor_chatbot import CropAdvisorChatbot
from app.services.vector_store.chroma_service import ChromaVectorStore

collection_name = "products"
embedding_function = get_embedding_function()


def get_vector_store() -> VectorStoreInterface:
    return ChromaVectorStore(
        collection_name=collection_name, embedding_function=embedding_function
    )


def get_conversation_manager(
    ai_client: AIClientInterface, ecommerce_service: EcommerceServiceInterface
) -> ConversationManager:
    return ConversationManager(ai_client=ai_client, ecommerce_service=ecommerce_service)


def get_ai_client() -> AIClientInterface:
    vector_store = get_vector_store()
    retriever = vector_store._vector_store.as_retriever()
    client = LangChainClientBuilder().with_retriever(retriever).build()
    return client


def get_crop_advisor_chatbot() -> ChatbotInterface:
    ai_client = get_ai_client()
    ecommerce_service = get_ecommerce_service()
    conversation_manager = get_conversation_manager(ai_client, ecommerce_service)
    return CropAdvisorChatbot(conversation_manager)
