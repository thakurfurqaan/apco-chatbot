from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma

from app.config import settings


class LangChainService:
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

    async def process_prompt(self, prompt: str) -> str:
        response = await self.qa_chain({"question": prompt})
        return response["answer"]
