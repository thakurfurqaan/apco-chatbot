from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import VectorStoreRetriever

from app.core.ai_client import AIClientInterface
from app.services.ai_client.langchain.dependencies import (
    get_llm,
    get_retriever_formatter,
    get_runnable,
)
from app.services.ai_client.langchain.dependencies.embedding import (
    get_embedding_function,
)
from app.services.ai_client.langchain.dependencies.prompt_template import (
    get_prompt_template,
)


class LangChainClient(AIClientInterface):
    def __init__(
        self,
        retriever: VectorStoreRetriever,
        embedding_function: Embeddings = None,
        llm: BaseChatModel = None,
    ):
        self.llm = llm or get_llm()
        self.embeddings = embedding_function or get_embedding_function()
        self.retriever = retriever
        self.retriever_formatter = get_retriever_formatter()

    def generate_response(self, prompt: str) -> str:
        rag_chain = self._get_rag_chain()
        response = rag_chain.invoke(prompt)
        return response

    def _get_rag_chain(self) -> str:
        context = self._construct_context()
        prompt = self._get_prompt()
        rag_chain = (
            {"context": context, "question": get_runnable()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        return rag_chain

    def _construct_context(self):
        return self.retriever | self.retriever_formatter

    def _get_prompt(self):
        return get_prompt_template()
