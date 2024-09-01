from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import BaseOutputParser
from langchain_core.prompts import ChatPromptTemplate

from app.core.ai_client import RAGChainCreator
from app.core.image_recognizer_service import ImageRecognizer


class ImageRecognizerRAGChainCreator(RAGChainCreator):

    def __init__(
        self,
        llm: BaseChatModel,
        prompt_template: ChatPromptTemplate,
        output_parser: BaseOutputParser,
    ):
        self._prompt_template = prompt_template
        self._llm = llm
        self._output_parser = output_parser

    def create_rag_chain(self):
        return self._prompt_template | self._llm | self._output_parser


class LangChainImageRecognizer(ImageRecognizer):

    def __init__(self, rag_chain_creator: RAGChainCreator):
        self._rag_chain_creator = rag_chain_creator

    def recognize(self, image_url: str) -> str:
        rag_chain = self._rag_chain_creator.create_rag_chain()
        response = rag_chain.invoke({"image_url": image_url})
        return response
