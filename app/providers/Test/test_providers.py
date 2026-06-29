from app.providers.memory_provider import MemoryProvider
from app.providers.provider_factory import ProviderFactory
from app.providers.base_provider import BaseProvider


def test_memory_provider_is_base_provider():
    provider = MemoryProvider()

    assert isinstance(provider, BaseProvider)


def test_memory_provider_get_all_workers():
    provider = MemoryProvider()

    result = provider.get_all("workers")

    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["worker_id"] == "W0001"
    assert result[0]["first_name"] == "Pablo"


def test_memory_provider_get_unknown_entity_returns_empty_list():
    provider = MemoryProvider()

    result = provider.get_all("unknown_entity")

    assert result == []


def test_memory_provider_get_worker_by_id():
    provider = MemoryProvider()

    result = provider.get_by_id("workers", "W0001")

    assert result is not None
    assert result["worker_id"] == "W0001"
    assert result["employee_id"] == "100001"


def test_memory_provider_get_unknown_worker_returns_none():
    provider = MemoryProvider()

    result = provider.get_by_id("workers", "W9999")

    assert result is None


def test_provider_factory_returns_memory_provider():
    provider = ProviderFactory.get_provider()

    assert isinstance(provider, MemoryProvider)
