import pytest

from app.services.ecommerce.ecommerce_mock.ecommerce_mock import EcommerceMockService


@pytest.mark.asyncio
async def test_ecommerce_service():
    service = EcommerceMockService()
    products = await service.get_all_products()
    assert isinstance(products, list)
