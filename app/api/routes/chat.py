from fastapi import APIRouter, Depends, File, UploadFile

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


@router.post("/chat/upload-image")
async def upload_image(
    file: UploadFile = File(...),
    chatbot: ChatbotInterface = Depends(get_crop_advisor_chatbot),
):
    contents = await file.read()
    # Process the image using your chatbot's image analysis capabilities
    response = chatbot.analyze_image(contents)
    return {"message": response}
