from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStore

from app.core.ai_service import AIClientInterface
from app.services.ai_client.langchain.dependencies import (
    get_llm,
    get_retriever_formatter,
    get_runnable,
)
from app.services.ai_client.langchain.dependencies.embedding import (
    get_embedding_function,
)


class LangChainClient(AIClientInterface):
    def __init__(
        self,
        vector_store: VectorStore = None,
        embedding_function: Embeddings = None,
        llm: BaseChatModel = None,
    ):
        self.vector_store = vector_store
        self.llm = llm or get_llm()
        self.embeddings = embedding_function or get_embedding_function()
        self.retriever = self.vector_store.as_retriever()
        self.retriever_formatter = get_retriever_formatter()

    def generate_response(self, prompt: str) -> str:
        rag_chain = self._get_rag_chain(prompt)
        response = rag_chain.invoke(prompt)
        return response

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
        return self.retriever | self.retriever_formatter
