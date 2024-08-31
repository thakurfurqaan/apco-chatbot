from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_chroma import Chroma
from langchain_openai import OpenAI, OpenAIEmbeddings

from app.config import settings
from app.core.ai_service import AIService


class LangChainOpenAIService(AIService):
    def __init__(self):
        self.llm = OpenAI(openai_api_key=settings.OPENAI_API_KEY)
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        self.db = Chroma(embedding_function=self.embeddings)
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            self.llm, self.db.as_retriever(), memory=self.memory
        )

    def process_prompt(self, prompt: str) -> str:
        response = self.qa_chain({"question": prompt})
        return response["answer"]
