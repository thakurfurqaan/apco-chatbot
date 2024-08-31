import pytest

from app.services.ai_client.langchain.client import LangChainService
from app.services.ecommerce.ecommerce_mock.ecommerce_mock import EcommerceMockService


@pytest.mark.asyncio
async def test_langchain_service():
    service = LangChainService()
    response = await service.process_prompt("What is the capital of France?")
    assert isinstance(response, str)
    assert len(response) > 0


@pytest.mark.asyncio
async def test_ecommerce_service():
    service = EcommerceMockService()
    products = await service.get_all_products()
    assert isinstance(products, list)
