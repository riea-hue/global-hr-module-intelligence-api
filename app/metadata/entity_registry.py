from app.metadata.metadata_loader import MetadataLoader


class EntityRegistry:
    def __init__(self, loader: MetadataLoader | None = None):
        self.loader = loader or MetadataLoader()
        self.entities = {
            entity["source_table"]: entity for entity in self.loader.get_entities()
        }

    def list_entities(self) -> list[str]:
        return list(self.entities.keys())

    def exists(self, entity_name: str) -> bool:
        return entity_name in self.entities

    def get(self, entity_name: str) -> dict | None:
        return self.entities.get(entity_name)

    def get_primary_key(self, entity_name: str) -> str | None:
        entity = self.get(entity_name)
        if not entity:
            return None

        return entity.get("primary_key_source_column")

    def get_domain(self, entity_name: str) -> str | None:
        entity = self.get(entity_name)
        if not entity:
            return None

        return entity.get("domain")

    def get_columns(self, entity_name: str) -> list[dict]:
        entity = self.get(entity_name)
        if not entity:
            return []

        return entity.get("attributes", [])

    def get_relationships(self, entity_name: str) -> list[dict]:
        if not self.exists(entity_name):
            return []

        return self.loader.get_relationships_for_entity(entity_name)

    def describe(self, entity_name: str) -> dict | None:
        entity = self.get(entity_name)

        if not entity:
            return None

        return {
            "source_table": entity.get("source_table"),
            "display_name": entity.get("display_name"),
            "domain": entity.get("domain"),
            "owner_team": entity.get("owner_team"),
            "primary_key": entity.get("primary_key_source_column"),
            "dataverse_entity": entity.get("dataverse_entity_logical_name"),
            "row_count": entity.get("row_count"),
            "column_count": entity.get("column_count"),
            "columns": self.get_columns(entity_name),
            "relationships": self.get_relationships(entity_name),
        }
