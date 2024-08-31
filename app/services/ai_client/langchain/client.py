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
        retriever_formatter=None,
        prompt_template=None,
        runnable=None,
        output_parser=None,
    ):
        self._llm = llm or get_llm()
        self._embeddings = embedding_function or get_embedding_function()
        self._retriever = retriever
        self._retriever_formatter = retriever_formatter or get_retriever_formatter()
        self._prompt_template = prompt_template or get_prompt_template()
        self._runnable = runnable or get_runnable()
        self._output_parser = output_parser or StrOutputParser()

    def generate_response(self, prompt: str) -> str:
        rag_chain = self._get_rag_chain()
        response = rag_chain.invoke(prompt)
        return response

    def _get_rag_chain(self) -> str:
        rag_chain = (
            {"context": self._construct_context(), "question": self._runnable}
            | self._prompt_template
            | self._llm
            | self._output_parser
        )
        return rag_chain

    def _construct_context(self):
        return self._retriever | self._retriever_formatter
