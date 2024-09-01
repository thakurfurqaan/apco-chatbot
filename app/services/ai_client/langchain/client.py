from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import BaseOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_core.vectorstores import VectorStore

from app.core.ai_client import AIClientInterface, ContextConstructor, RAGChainCreator


class DefaultContextConstructor(ContextConstructor):
    def __init__(self, vector_store: VectorStore, retriever_formatter):
        self._vector_store = vector_store
        self._retriever_formatter = retriever_formatter

    def construct_context(self):
        return self._vector_store.as_retriever() | self._retriever_formatter


class DefaultRAGChainCreator(RAGChainCreator):
    def __init__(
        self,
        context_constructor: ContextConstructor,
        llm: BaseChatModel,
        prompt_template: ChatPromptTemplate,
        output_parser: BaseOutputParser,
        runnable: Runnable,
    ):
        self._context_constructor = context_constructor
        self._runnable = runnable
        self._prompt_template = prompt_template
        self._llm = llm
        self._output_parser = output_parser

    def create_rag_chain(self):
        return (
            {
                "context": self._context_constructor.construct_context(),
                "question": self._runnable,
            }
            | self._prompt_template
            | self._llm
            | self._output_parser
        )


class LangChainClient(AIClientInterface):
    def __init__(
        self,
        context_constructor: ContextConstructor,
        rag_chain_creator: RAGChainCreator,
    ):
        self._context_constructor = context_constructor
        self._rag_chain_creator = rag_chain_creator

    def generate_response(self, prompt: str) -> str:
        rag_chain = self._rag_chain_creator.create_rag_chain()
        response = rag_chain.invoke(str(prompt))
        return response
