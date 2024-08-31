from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from app.config import settings

llm = ChatOpenAI(model=settings.OPENAI_CHAT_MODEL, api_key=settings.OPENAI_API_KEY)


def get_llm() -> BaseChatModel:
    return llm
