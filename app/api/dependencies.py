from app.core.conversation_manager import ConversationManager
from app.core.ecommerce_service import EcommerceService


def get_conversation_manager() -> ConversationManager:
    from app.main import conversation_manager

    return conversation_manager


def get_ecommerce_service() -> EcommerceService:
    from app.main import ecommerce_service

    return ecommerce_service
