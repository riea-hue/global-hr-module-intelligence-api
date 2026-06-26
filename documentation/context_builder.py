from pathlib import Path
import json
from datetime import datetime

from documentation.markdown_renderer import (
    build_architecture_diagram,
    build_features_list,
    build_markdown_table,
    build_odata_diagram,
    build_rbac_diagram,
)


BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_METADATA_FILE = (
    BASE_DIR / "metadata" / "global_hr_dataverse_metadata_model.json"
)

DEFAULT_RELATIONSHIP_FILE = (
    BASE_DIR / "metadata" / "global_hr_relationship_matrix_v1.json"
)

FRAMEWORK_VERSION = "1.0.0"


class DocumentationContextBuilder:
    """
    Builds reusable documentation context from Global HR metadata files.
    """

    def __init__(
        self,
        metadata_file: Path | None = None,
        relationship_file: Path | None = None,
    ):
        self.metadata_file = metadata_file or DEFAULT_METADATA_FILE
        self.relationship_file = relationship_file or DEFAULT_RELATIONSHIP_FILE

    def build(self) -> dict:
        metadata = self._load_json(self.metadata_file)
        relationships = self._load_json_optional(self.relationship_file)

        entities = metadata.get("entities", [])
        domains = metadata.get("domains", [])
        summary = metadata.get("summary", {})

        relationship_items = relationships.get("relationships", [])

        return {
            "project_name": "Global HR Intelligence API",
            "project_description": (
                "Metadata-driven Enterprise HR API Starter Kit built with FastAPI, "
                "OData-style query support, RBAC, generated routers, OpenAPI enrichment, "
                "and governed HR metadata."
            ),
            "version": FRAMEWORK_VERSION,
            "generated_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "entity_count": summary.get("table_count", len(entities)),
            "domain_count": summary.get("domain_count", len(domains)),
            "relationship_count": summary.get(
                "relationship_count",
                len(relationship_items),
            ),
            "entities": entities,
            "domains": domains,
            "relationships": relationship_items,
            "features": build_features_list(),
            "domains_table": self._build_domains_table(domains),
            "entities_table": self._build_entities_table(entities),
            "relationships_table": self._build_relationships_table(
                relationship_items[:25]
            ),
            "architecture_diagram": build_architecture_diagram(),
            "rbac_diagram": build_rbac_diagram(),
            "odata_diagram": build_odata_diagram(),
            "roadmap": self._build_roadmap(),
        }

    def _build_domains_table(self, domains: list[dict]) -> str:
        rows = []

        for domain in domains:
            rows.append(
                [
                    domain.get("domain", ""),
                    domain.get("owner_team", ""),
                    ", ".join(domain.get("allowed_departments", [])),
                ]
            )

        return build_markdown_table(
            ["Domain", "Owner Team", "Allowed Departments"],
            rows,
        )

    def _build_entities_table(self, entities: list[dict]) -> str:
        rows = []

        for entity in entities:
            rows.append(
                [
                    f"`{entity.get('source_table', '')}`",
                    entity.get("domain", ""),
                    entity.get("owner_team", ""),
                    f"`{entity.get('primary_key_source_column', '')}`",
                    entity.get("dataverse_entity_logical_name", ""),
                ]
            )

        return build_markdown_table(
            [
                "Entity",
                "Domain",
                "Owner Team",
                "Primary Key",
                "Dataverse Logical Name",
            ],
            rows,
        )

    def _build_relationships_table(self, relationships: list[dict]) -> str:
        if not relationships:
            return "_No relationship metadata found._"

        rows = []

        for relationship in relationships:
            rows.append(
                [
                    relationship.get("relationship_id", ""),
                    relationship.get("source_table", ""),
                    relationship.get("source_column", ""),
                    relationship.get("target_table", ""),
                    relationship.get("target_column", ""),
                    relationship.get("cardinality", ""),
                    relationship.get("domain", ""),
                ]
            )

        return build_markdown_table(
            [
                "ID",
                "Source Table",
                "Source Column",
                "Target Table",
                "Target Column",
                "Cardinality",
                "Domain",
            ],
            rows,
        )

    def _build_roadmap(self) -> str:
        return """### v1.0 Core

- Metadata-driven FastAPI framework
- Generated Pydantic models and routers
- OData-style query support
- Department-based RBAC
- Metadata API
- OpenAPI governance enrichment
- Metadata-driven smoke test suite
- Documentation Engine

### v1.5 Enterprise Foundation

- pytest integration
- coverage reports
- GitHub Actions CI/CD
- Dockerfile and docker-compose
- PostgreSQL / SQL Server / Dataverse data providers
- Metadata schema validation

### v2.0 Enterprise Edition

- JWT / OAuth2 / Microsoft Entra ID
- SDK generation for Python, C#, and TypeScript
- `$expand` support
- AI-assisted metadata catalog
- Enterprise documentation portal
"""

    @staticmethod
    def _load_json(path: Path) -> dict:
        if not path.exists():
            raise FileNotFoundError(f"Metadata file not found: {path}")

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def _load_json_optional(path: Path) -> dict:
        if not path.exists():
            return {}

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)