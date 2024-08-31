from fastapi import APIRouter, Depends

from app.api.dependencies.crop_advisor_chatbot import get_crop_advisor_chatbot
from app.core.chatbot_service import ChatbotInterface
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    chatbot: ChatbotInterface = Depends(get_crop_advisor_chatbot),
):
    message = chatbot.query(request.message)
    return ChatResponse(message=message)
