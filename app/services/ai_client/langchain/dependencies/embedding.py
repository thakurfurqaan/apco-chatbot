from langchain_core.embeddings import Embeddings
from langchain_openai import OpenAIEmbeddings

from app.config import settings

embedding_function = OpenAIEmbeddings(
    model=settings.OPENAI_EMBEDDING_MODEL, api_key=settings.OPENAI_API_KEY
)


def get_embedding_function() -> Embeddings:
    return embedding_function
