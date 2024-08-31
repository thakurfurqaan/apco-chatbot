from typing import Type

from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain

from app.core.ai_service import AIService


class LangChainAIBase(AIService):
    def __init__(
        self,
        llm: Type[LLM],
        vector_store: Type[VectorStore],
        memory: Type[Memory],
        qa_chain_cls: Type[BaseConversationalRetrievalChain],
    ):
        self.llm = llm
        self.vector_store = vector_store
        self.memory = memory
        self.qa_chain = qa_chain_cls.from_llm(
            self.llm, self.vector_store.as_retriever(), memory=self.memory
        )

    def process_prompt(self, prompt: str) -> str:
        response = self.qa_chain({"question": prompt})
        return response["answer"]
