# TODO: write your code here
# ------------------------------------


# AI Module
# Interface for AI client.
from abc import ABC, abstractmethod


class LLM(ABC):

    @abstractmethod
    def send_message(self):
        pass

    def list_messages(self):
        pass


class GPT4(LLM):

    def __init__(self):
        pass


class AIService(ABC):

    @abstractmethod
    def process_prompt(self):
        pass


class LLMResponseFormatter(ABC):

    def format_response(self, response):
        pass


class LangChainService(AIService):

    def __init__(self, model, vector_store, formatter: LLMResponseFormatter):
        pass

    def process_prompt(self, response):
        return self.formatter(response)

    def _format_response(self, response):
        pass


# E-commerce Module
# Mock implementation of EcommerceServiceInterface for testing


class IVectorStore(ABC):

    @abstractmethod
    def retrieve_vectors(self):
        pass


class ChromaDB(IVectorStore):

    def retrieve_vectors(self, prompt: str):
        pass


class EcommerceServiceInterface(ABC):

    @abstractmethod
    def get_all_products(self):
        pass


class EcommerceService1(EcommerceServiceInterface):

    def get_all_products(self):
        pass


# Conversation Manager
class ConversationManager:
    """Handles the conversation logic and coordinates between AI and E-commerce modules."""

    def __init__(self, llm_service, ecommerce_service: EcommerceServiceInterface):
        self.llm_service = llm_service
        self.ecommerce_service = ecommerce_service

    def send_message(self):
        product_data = self.ecommerce_service.get_all_products()
        response = self.llm_service(product_data, prompt)
        return self._format_response(response)

    def _format_response(self, response: str):
        return response.strip().replace("*", "")


# Chatbot Interface
class LLM(ABC):
    """AI-powered chatbot for diagnosing and treating crop diseases."""

    @abstractmethod
    def send_message(self, message):
        pass


class Image:

    def get_image_data(self):
        pass


class ImageRecognizer(ABC):

    def recognize(self):
        pass


class GPT4Image(ImageRecognizer):

    def __init__(self, **kwargs):
        self.image_compressor = image_compressor
        self.file_object_creator = file_object_creator

    def recognize(self):
        pass

    def _compress_image(self):

        pass

    def _create_file_object(self):
        pass


class LLMs(Enum):

    GPT4_TURBO = auto()


class ImageRecognizers(Enum):

    GPT4_IMAGE = auto()


def product_list_response_formatter(response):
    pass


# ------------------------------------
if __name__ == "__main__":
    # Step 1: Instantiate OpenAIClient with a mock API key
    vector_store: IVectorStore = ChromaDB()
    ai_service: AIService = LangChainService(
        vector_store=vector_store, model=LLMs.GPT4_TURBO
    )
    image_recognizer_service: ImageRecognizer = GPT4Image()
    image_response = image_recognizer_service.recognize(image_data)
    ecommerce_service: EcommerceServiceInterface = EcommerceService1()
    response = ai_service.process_prompt()
    formatted_response = product_list_response_formatter(response)

    # Step 2: Instantiate MockEcommerceService

    # Step 3: Create a ConversationManager instance using the above instances

    # Step 4: Create a ChatBot instance using the ConversationManager

    # Example usage for text and image input
