from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, File, UploadFile

from app.api.dependencies.containers import Container
from app.core.chatbot import ChatbotInterface
from app.core.image_processor import ImageProcessorInterface
from app.core.image_recognizer_service import ImageRecognizer
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


def response_formatter(response: str):
    # For any formatting requirements, nothing for now
    return response


@router.post("/chat", response_model=ChatResponse)
@inject
def chat(
    request: ChatRequest,
    chatbot: ChatbotInterface = Depends(Provide[Container.crop_disease_chatbot]),
):
    """
    Send a message to the chatbot and get a response.
    """
    response = chatbot.send_message(request.message)
    formatted_response = response_formatter(response)
    return ChatResponse(message=formatted_response)


@router.post("/chat/analyze-image")
@inject
async def analyze_image(
    file: UploadFile = File(...),
    image_recognizer: ImageRecognizer = Depends(Provide[Container.image_recognizer]),
    image_processor: ImageProcessorInterface = Depends(
        Provide[Container.image_processor]
    ),
):
    data_url = await image_processor.get_data_url(file)
    response = image_recognizer.recognize(image_url=data_url)
    return {"message": response}
