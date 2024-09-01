from typing import Annotated

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, File, Form, UploadFile

from app.api.dependencies.containers import Container
from app.core.chatbot import ChatbotInterface
from app.core.image_analyzer import ImageAnalyzerInterface
from app.schemas.chat import ChatResponse, ImageAnalysisResponse

router = APIRouter()


def response_formatter(response: str):
    # For any formatting requirements, nothing for now
    return response


@router.post("/chat", response_model=ChatResponse)
@inject
async def chat(
    message: Annotated[str, Form()],
    file: UploadFile = File(None),
    chatbot: ChatbotInterface = Depends(Provide[Container.crop_disease_chatbot]),
    image_analyzer: ImageAnalyzerInterface = Depends(Provide[Container.image_analyzer]),
):
    """
    Send a message to the chatbot and get a response.
    """
    user_prompt = message
    if file:
        image_analysis = await image_analyzer.analyze(file)
        user_prompt += f"\nImage analysis: {image_analysis}"
    response = chatbot.send_message(user_prompt)
    formatted_response = response_formatter(response)
    return ChatResponse(message=formatted_response)


@router.post("/chat/analyze-image", response_model=ImageAnalysisResponse)
@inject
async def analyze_image(
    file: UploadFile = File(...),
    image_analyzer: ImageAnalyzerInterface = Depends(Provide[Container.image_analyzer]),
):
    response = await image_analyzer.analyze(file)
    return ImageAnalysisResponse(description=response)
