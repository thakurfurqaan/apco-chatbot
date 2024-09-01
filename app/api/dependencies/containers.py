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
from app.services.ai_client.langchain.client import LangChainClientBuilder
from app.services.ai_client.langchain.formatters import default_retriever_formatter
from app.services.chatbot.crop_advisor_chatbot import CropAdvisorChatbot
from app.services.ecommerce.ecommerce_mock.ecommerce_mock import EcommerceMockService
from app.services.vector_store.chroma_vector_store import ChromaVectorStore


class Container(containers.DeclarativeContainer):
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

    # Vector store
    product_vector_store = providers.Singleton(
        ChromaVectorStore,
        collection_name=config.PRODUCT_VECTOR_STORE_COLLECTION_NAME,
        embedding_function=embedding_function,
        persist_directory=config.CHROMA_DB_PATH,
    )

    # Ecommerce service
    ecommerce_service = providers.Singleton(EcommerceMockService)

    # AI client
    def build_langchain_client(pvs, rf, l, pt, r, op):
        return (
            LangChainClientBuilder()
            .with_retriever(pvs.as_retriever())
            .with_retriever_formatter(rf)
            .with_prompt_template(pt)
            .with_llm(l)
            .with_runnable(r)
            .with_output_parser(op)
            .build()
        )

    ai_client: providers.Provider[AIClientInterface] = providers.Factory(
        build_langchain_client,
        pvs=langchain_product_vector_store,
        rf=retriever_formatter,
        l=llm,
        pt=prompt_template,
        r=runnable,
        op=output_parser,
    )

    # Conversation manager
    conversation_manager = providers.Singleton(
        ConversationManager, ai_client=ai_client, ecommerce_service=ecommerce_service
    )

    # Crop advisor chatbot
    crop_advisor_chatbot = providers.Singleton(
        CropAdvisorChatbot, conversation_manager=conversation_manager
    )
