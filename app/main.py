from fastapi import FastAPI
from langchain_chroma import Chroma

from app.api.routes import chat, ecommerce
from app.config import settings
from app.core.conversation_manager import ConversationManager
from app.services.ai.langchain.langchain_service import LangChainOpenAIService
from app.services.ecommerce.ecommerce_mock import EcommerceMockService

app = FastAPI()

# vector_store_service = ChromaService()
vector_store = Chroma(
    collection_name=settings.PRODUCT_VECTOR_STORE_COLLECTION_NAME,
    persist_directory=settings.CHROMA_DB_PATH,
)

ai_service = LangChainOpenAIService(vector_store)
ecommerce_service = EcommerceMockService()
conversation_manager = ConversationManager(ai_service, ecommerce_service)

app.include_router(chat.router)
app.include_router(ecommerce.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
