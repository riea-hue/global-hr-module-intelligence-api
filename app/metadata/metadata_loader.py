import json
from pathlib import Path


class MetadataLoader:
    def __init__(self, metadata_dir: str = "metadata"):
        self.metadata_dir = Path(metadata_dir)
        self.dataverse_model = self._load_json(
            "global_hr_dataverse_metadata_model.json"
        )
        self.relationship_matrix = self._load_json(
            "global_hr_relationship_matrix_v1.json"
        )
        self.security_model = self._load_json("global_hr_security_model.json")
        self.department_access = self._load_json("department_access_catalog.json")

    def _load_json(self, filename: str) -> dict:
        file_path = self.metadata_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Metadata file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_summary(self) -> dict:
        summary = self.dataverse_model.get("summary", {})

        return {
            "project": self.dataverse_model.get("project"),
            "version": self.dataverse_model.get("version"),
            "tables": summary.get("table_count"),
            "relationships": summary.get("relationship_count"),
            "domains": summary.get("domain_count"),
        }

    def get_entities(self) -> list[dict]:
        return self.dataverse_model.get("entities", [])

    def get_entity(self, entity_name: str) -> dict | None:
        for entity in self.get_entities():
            if entity.get("source_table") == entity_name:
                return entity

        return None

    def get_domains(self) -> list[dict]:
        return self.dataverse_model.get("domains", [])

    def get_relationships_for_entity(self, entity_name: str) -> list[dict]:
        relationships = self.relationship_matrix.get("relationships", [])

        return [
            relationship
            for relationship in relationships
            if relationship.get("source_table") == entity_name
            or relationship.get("target_table") == entity_name
        ]

    def get_entity_names(self) -> list[str]:
        return [entity["source_table"] for entity in self.get_entities()]

    def entity_exists(self, entity_name: str) -> bool:
        return entity_name in self.get_entity_names()
