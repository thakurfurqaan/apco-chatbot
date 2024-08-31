from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = ""
    OPENAI_API_KEY: str = ""
    CHROMA_DB_PATH: str = ""
    OPENAI_EMBEDDING_MODEL: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
