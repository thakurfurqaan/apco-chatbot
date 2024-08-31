from typing import Callable

from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStore

from app.core.ai_service import AIService
from app.services.ai.langchain.docs_formatter import get_docs_formatter
from app.services.ai.langchain.embedding import get_embedding_function
from app.services.ai.langchain.llm import get_llm
from app.services.ai.langchain.runnable import get_runnable


class LangChainOpenAIService(AIService):
    def __init__(
        self,
        vector_store: VectorStore = None,
        response_formatting_function: Callable = None,
    ):
        self.llm = get_llm()
        self.embeddings = get_embedding_function()
        self.vector_store = vector_store
        self.retriever = self.vector_store.as_retriever()
        self.response_formatting_function = response_formatting_function
        self.docs_formatter = get_docs_formatter()

    def process_prompt(self, prompt: str) -> str:
        rag_chain = self._get_rag_chain(prompt)
        response = rag_chain.invoke(prompt)
        return self.response_formatting_function(response)

    def _get_rag_chain(self, prompt: str) -> str:
        context = self._construct_context()
        rag_chain = (
            {"context": context, "question": get_runnable()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        return rag_chain

    def _construct_context(self):
        return self.retriever | self.docs_formatter
