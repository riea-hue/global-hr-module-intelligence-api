from app.providers.memory_provider import MemoryProvider


class ProviderFactory:
    @staticmethod
    def get_provider():

        return MemoryProvider()
