from pathlib import Path
import json

from fastapi.openapi.utils import get_openapi


FRAMEWORK_NAME = "Global HR Intelligence API"
FRAMEWORK_VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent.parent
METADATA_FILE = BASE_DIR / "metadata" / "global_hr_dataverse_metadata_model.json"


def enrich_openapi(app, metadata_loader=None):
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = get_openapi(
            title="Global HR Intelligence API",
            version=FRAMEWORK_VERSION,
            description=(
                "Metadata-driven Enterprise HR API Starter Kit with FastAPI, "
                "OData-style query support, RBAC, generated routers, and governed "
                "HR data product metadata."
            ),
            routes=app.routes,
        )

        entities = load_entities(metadata_loader)
        entity_map = build_entity_map(entities)

        for path, path_item in openapi_schema.get("paths", {}).items():
            entity_name = extract_entity_from_path(path)

            if not entity_name:
                continue

            entity_metadata = entity_map.get(entity_name)

            if not entity_metadata:
                continue

            for method, operation in path_item.items():
                if method.lower() not in ["get", "post", "put", "patch", "delete"]:
                    continue

                enrich_operation(operation, entity_metadata)

        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi


def load_entities(metadata_loader=None):
    if metadata_loader is not None:
        for method_name in [
            "get_entities",
            "load_entities",
            "get_all_entities",
            "load_metadata",
            "get_metadata",
        ]:
            if hasattr(metadata_loader, method_name):
                result = getattr(metadata_loader, method_name)()

                if isinstance(result, list):
                    return result

                if isinstance(result, dict) and "entities" in result:
                    return result["entities"]

    if not METADATA_FILE.exists():
        return []

    with open(METADATA_FILE, "r", encoding="utf-8") as file:
        metadata = json.load(file)

    return metadata.get("entities", [])


def build_entity_map(entities):
    entity_map = {}

    for entity in entities:
        source_table = entity.get("source_table")

        if source_table:
            entity_map[source_table] = entity

        dataverse_name = entity.get("dataverse_entity_logical_name")

        if dataverse_name:
            entity_map[dataverse_name] = entity

    return entity_map


def extract_entity_from_path(path: str):
    parts = path.strip("/").split("/")

    if len(parts) >= 3 and parts[0] == "api" and parts[1] == "v1":
        entity = parts[2]

        if entity.startswith("$"):
            return None

        return entity

    return None


def enrich_operation(operation, entity_metadata):
    source_table = entity_metadata.get("source_table")
    domain = entity_metadata.get("domain")
    owner_team = entity_metadata.get("owner_team")
    allowed_departments = entity_metadata.get("allowed_departments", [])

    operation["x-framework"] = FRAMEWORK_NAME
    operation["x-framework-version"] = FRAMEWORK_VERSION
    operation["x-generated"] = True
    operation["x-generated-by"] = "router_generator.py"
    operation["x-signature"] = build_signature(entity_metadata)

    operation["x-source-table"] = source_table
    operation["x-domain"] = domain
    operation["x-owner-team"] = owner_team
    operation["x-data-product-id"] = entity_metadata.get("data_product_id")
    operation["x-data-classification"] = (
        entity_metadata.get("classification")
        or entity_metadata.get("data_classification")
        or "Internal"
    )
    operation["x-allowed-departments"] = allowed_departments

    operation["x-rbac"] = {
        "enabled": True,
        "header": "X-Department",
        "allowed_departments": allowed_departments,
    }

    if domain:
        operation["tags"] = [domain]


def build_signature(entity_metadata: dict) -> str:
    source_table = entity_metadata.get("source_table", "unknown")
    domain = entity_metadata.get("domain", "unknown")
    owner_team = entity_metadata.get("owner_team", "unknown")
    data_product_id = entity_metadata.get("data_product_id", "unknown")

    return f"ghr::{source_table}::{domain}::{owner_team}::{data_product_id}"