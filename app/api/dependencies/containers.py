from dependency_injector import containers, providers
from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_core.embeddings import Embeddings
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from app.config import settings
from app.core.ai_client import AIClientInterface
from app.core.conversation_manager import ConversationManager
from app.prompts.crop_advisor_prompt import template
from app.services.ai_client.langchain.client import (
    DefaultContextConstructor,
    DefaultRAGChainCreator,
    LangChainClient,
)
from app.services.ai_client.langchain.formatters import default_retriever_formatter
from app.services.chatbot.crop_advisor_chatbot import CropAdvisorChatbot
from app.services.ecommerce.ecommerce_mock.ecommerce_mock import EcommerceMockService
from app.services.vector_store.langchain_chroma_vector_store import LangChainChromaVS


class Container(containers.DeclarativeContainer):
    """Container for the application."""

    config = providers.Configuration()
    json_config = settings.model_dump(mode="json")
    config.from_dict(json_config)

    # Langchain dependencies
    embedding_function: providers.Provider[Embeddings] = providers.Factory(
        OpenAIEmbeddings,
        model=config.OPENAI_EMBEDDING_MODEL,
        api_key=config.OPENAI_API_KEY,
    )

    llm: providers.Provider[BaseChatModel] = providers.Factory(
        ChatOpenAI,
        model=config.OPENAI_CHAT_MODEL,
        api_key=config.OPENAI_API_KEY,
    )

    prompt_template = providers.Factory(
        ChatPromptTemplate.from_template, template=template
    )

    runnable: providers.Provider[RunnablePassthrough] = providers.Factory(
        RunnablePassthrough
    )

    retriever_formatter = providers.Object(default_retriever_formatter)

    output_parser = providers.Factory(StrOutputParser)

    langchain_product_vector_store = providers.Singleton(
        Chroma,
        collection_name=config.PRODUCT_VECTOR_STORE_COLLECTION_NAME,
        embedding_function=embedding_function,
        persist_directory=config.CHROMA_DB_PATH,
    )

    # LangChain AI client
    _context_constructor = providers.Factory(
        DefaultContextConstructor,
        vector_store=langchain_product_vector_store,
        retriever_formatter=retriever_formatter,
    )
    _rag_chain_creator = providers.Factory(
        DefaultRAGChainCreator,
        context_constructor=_context_constructor,
        runnable=runnable,
        prompt_template=prompt_template,
        llm=llm,
        output_parser=output_parser,
    )
    ai_client: providers.Provider[AIClientInterface] = providers.Factory(
        LangChainClient,
        context_constructor=_context_constructor,
        rag_chain_creator=_rag_chain_creator,
    )

    # Vector store
    product_vector_store = providers.Singleton(
        LangChainChromaVS,
        collection_name=config.PRODUCT_VECTOR_STORE_COLLECTION_NAME,
        embedding_function=embedding_function,  # Same embedding function as the one used for the RAG chain
        persist_directory=config.CHROMA_DB_PATH,
    )

    # Ecommerce service
    ecommerce_service = providers.Singleton(EcommerceMockService)

    # Conversation manager
    conversation_manager = providers.Singleton(
        ConversationManager,
        ai_client=ai_client,
        ecommerce_service=ecommerce_service,
    )

    # Crop advisor chatbot
    crop_disease_chatbot = providers.Singleton(
        CropAdvisorChatbot, conversation_manager=conversation_manager
    )
