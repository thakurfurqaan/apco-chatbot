from typing import Callable

from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import VectorStoreRetriever

from app.core.ai_client import AIClientInterface, ContextConstructor, RAGChainCreator


class DefaultContextConstructor(ContextConstructor):
    def __init__(self, retriever: VectorStoreRetriever, retriever_formatter):
        self._retriever = retriever
        self._retriever_formatter = retriever_formatter

    def construct_context(self):
        return self._retriever | self._retriever_formatter


class DefaultRAGChainCreator(RAGChainCreator):
    def __init__(
        self,
        context_constructor: ContextConstructor,
        llm: BaseChatModel,
        prompt_template,
        output_parser: StrOutputParser,
        runnable,
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
        response = rag_chain.invoke(prompt)
        return response


class LangChainClientBuilder:
    def __init__(self):
        self._retriever: VectorStoreRetriever = None
        self._embedding_function: Embeddings = None
        self._llm: BaseChatModel = None
        self._retriever_formatter: Callable = None
        self._prompt_template: ChatPromptTemplate = None
        self._runnable = None
        self._output_parser = None

    def with_retriever(self, retriever):
        self._retriever = retriever
        return self

    def with_embedding_function(self, embedding_function):
        self._embedding_function = embedding_function
        return self

    def with_llm(self, llm):
        self._llm = llm
        return self

    def with_retriever_formatter(self, retriever_formatter):
        self._retriever_formatter = retriever_formatter
        return self

    def with_prompt_template(self, prompt_template):
        self._prompt_template = prompt_template
        return self

    def with_runnable(self, runnable):
        self._runnable = runnable
        return self

    def with_output_parser(self, output_parser):
        self._output_parser = output_parser
        return self

    def build(self):

        context_constructor = DefaultContextConstructor(
            self._retriever, self._retriever_formatter
        )
        rag_chain_creator = DefaultRAGChainCreator(
            context_constructor,
            self._runnable,
            self._prompt_template,
            self._llm,
            self._output_parser,
        )

        return LangChainClient(context_constructor, rag_chain_creator)
