from app.core.conversation_manager import ConversationManager


def get_conversation_manager() -> ConversationManager:
    from app.main import conversation_manager

    return conversation_manager
