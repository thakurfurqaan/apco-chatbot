from fastapi import FastAPI

from app.api.routes import chat, ecommerce
from app.core.ai_service import AIService
from app.core.conversation_manager import ConversationManager
from app.core.ecommerce_service import EcommerceService

app = FastAPI()

ai_service = AIService()
ecommerce_service = EcommerceService()
conversation_manager = ConversationManager(ai_service, ecommerce_service)

app.include_router(chat.router)
app.include_router(ecommerce.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
