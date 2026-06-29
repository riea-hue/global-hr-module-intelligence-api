from abc import ABC, abstractmethod


class BaseProvider(ABC):
    @abstractmethod
    def get_all(self, entity_name: str):
        pass

    @abstractmethod
    def get_by_id(self, entity_name: str, entity_id: str):
        pass
