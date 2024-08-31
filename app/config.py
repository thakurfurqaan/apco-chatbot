from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    OPENAI_API_KEY: str = ""
    OPENAI_CHAT_MODEL: str = "gpt-4o-mini"
    CHROMA_DB_PATH: str = ""
    OPENAI_EMBEDDING_MODEL: str = ""
    PRODUCT_VECTOR_STORE_COLLECTION_NAME: str = "products"

    class Config:
        env_file = ".env"


settings = Settings()
