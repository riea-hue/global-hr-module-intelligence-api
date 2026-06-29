from fastapi import APIRouter

from app.core.services import entity_registry
from app.providers.provider_factory import ProviderFactory


class DynamicRouterGenerator:
    def __init__(self):
        self.provider = ProviderFactory.get_provider()

        self.router = APIRouter(
            prefix="/entities",
            tags=["Entities"],
        )

        self.generate()

    def generate(self):
        for entity_name in entity_registry.list_entities():
            self.router.add_api_route(
                path=f"/{entity_name}",
                endpoint=self.build_collection_endpoint(entity_name),
                methods=["GET"],
                name=f"get_{entity_name}",
            )

            self.router.add_api_route(
                path=f"/{entity_name}/{{entity_id}}",
                endpoint=self.build_detail_endpoint(entity_name),
                methods=["GET"],
                name=f"get_{entity_name}_by_id",
            )

    def build_collection_endpoint(self, entity_name: str):
        def endpoint():
            metadata = entity_registry.describe(entity_name)
            rows = self.provider.get_all(entity_name)

            return {
                "entity": entity_name,
                "count": len(rows),
                "provider": self.provider.__class__.__name__,
                "data": rows,
                "metadata": metadata,
                "message": "Dynamic collection endpoint generated from metadata.",
            }

        return endpoint

    def build_detail_endpoint(self, entity_name: str):
        def endpoint(entity_id: str):
            metadata = entity_registry.describe(entity_name)
            row = self.provider.get_by_id(entity_name, entity_id)

            if row is None:
                return {
                    "entity": entity_name,
                    "entity_id": entity_id,
                    "found": False,
                    "provider": self.provider.__class__.__name__,
                    "data": None,
                    "metadata": metadata,
                    "message": "Record not found.",
                }

            return {
                "entity": entity_name,
                "entity_id": entity_id,
                "found": True,
                "provider": self.provider.__class__.__name__,
                "data": row,
                "metadata": metadata,
                "message": "Dynamic detail endpoint generated from metadata.",
            }

        return endpoint


dynamic_router = DynamicRouterGenerator().router
