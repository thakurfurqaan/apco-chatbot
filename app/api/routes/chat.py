from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.api.dependencies.containers import Container
from app.core.chatbot import ChatbotInterface
from app.core.image_analyzer import ImageAnalyzerInterface
from app.schemas.chat import ChatRequest, ChatResponse, ImageAnalysisRequest

router = APIRouter()


def response_formatter(response: str):
    # For any formatting requirements, nothing for now
    return response


@router.post("/chat", response_model=ChatResponse)
@inject
def chat(
    chat_request: ChatRequest,
    chatbot: ChatbotInterface = Depends(Provide[Container.crop_disease_chatbot]),
    image_analyzer: ImageAnalyzerInterface = Depends(Provide[Container.image_analyzer]),
):
    """
    Send a message to the chatbot and get a response.
    """
    user_prompt = chat_request.message
    if chat_request.file:
        image_analysis = image_analyzer.analyze(chat_request.file)
        user_prompt += f"Image analysis: {image_analysis}"
    response = chatbot.send_message(user_prompt)
    formatted_response = response_formatter(response)
    return ChatResponse(message=formatted_response)


@router.post("/chat/analyze-image")
@inject
async def analyze_image(
    request: ImageAnalysisRequest,
    image_analyzer: ImageAnalyzerInterface = Depends(Provide[Container.image_analyzer]),
):
    response = image_analyzer.analyze(request.file)
    return {"description": response}
