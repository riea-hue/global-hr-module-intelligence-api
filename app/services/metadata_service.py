from engine.generators.metadata_loader import MetadataLoader


class MetadataService:
    def __init__(self):
        self.loader = MetadataLoader()

    def list_entities(self) -> list[dict]:
        resources = self.loader.api_catalog.get("resources", [])

        return [
            {
                "entity": resource.get("source_table"),
                "domain": resource.get("domain"),
                "owner_team": resource.get("owner_team"),
                "classification": resource.get("classification"),
                "base_path": f"/api/v1/{resource.get('source_table')}",
            }
            for resource in resources
            if resource.get("source_table")
        ]

    def get_entity(self, entity_name: str) -> dict:
        return self.loader.build_entity_definition(entity_name)

    def get_catalog(self) -> dict:
        entities = self.list_entities()

        return {
            "name": "Global HR Intelligence API Metadata Catalog",
            "version": "1.0.0",
            "entity_count": len(entities),
            "entities": entities,
        }
