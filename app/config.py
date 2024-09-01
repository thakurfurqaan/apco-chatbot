from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    CHROMA_DB_PATH: str = ""
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-large"
    OPENAI_CHAT_MODEL: str = "gpt-4o-mini"
    PRODUCT_VECTOR_STORE_COLLECTION_NAME: str = "products"

    class Config:
        env_file = ".env"


settings = Settings()
