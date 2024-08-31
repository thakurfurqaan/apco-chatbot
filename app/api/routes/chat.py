from fastapi import APIRouter, Depends

from app.api.dependencies.crop_advisor_chatbot import get_crop_advisor_chatbot
from app.core.chatbot import ChatbotInterface
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


def response_formatter(response: str):
    # For any formatting requirements, nothing for now
    return response


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    chatbot: ChatbotInterface = Depends(get_crop_advisor_chatbot),
):
    response = chatbot.send_message(request.message)
    formatted_response = response_formatter(response)
    return ChatResponse(message=formatted_response)
