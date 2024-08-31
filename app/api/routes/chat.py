from fastapi import APIRouter, Depends

from app.api.dependencies import get_conversation_manager
from app.core.conversation_manager import ConversationManager
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat/products/query", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    conversation_manager: ConversationManager = Depends(get_conversation_manager),
):
    response = conversation_manager.send_message(request.message)
    return ChatResponse(message=response)
