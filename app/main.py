from fastapi import FastAPI

from app.api.routes import chat, ecommerce
from app.core.conversation_manager import ConversationManager
from app.services.ai.langchain_service import LangChainService
from app.services.ecommerce.ecommerce_mock import EcommerceMockService

app = FastAPI()

ai_service = LangChainService()
ecommerce_service = EcommerceMockService()
conversation_manager = ConversationManager(ai_service, ecommerce_service)

app.include_router(chat.router)
app.include_router(ecommerce.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
