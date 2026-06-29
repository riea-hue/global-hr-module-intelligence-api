from fastapi import APIRouter, HTTPException

from app.metadata.metadata_loader import MetadataLoader

from app.metadata.entity_registry import EntityRegistry


router = APIRouter(prefix="/metadata", tags=["Metadata"])

loader = MetadataLoader()

registry = EntityRegistry(loader)


@router.get("")
def get_metadata_summary():
    return loader.get_summary()


@router.get("/entities")
def get_entities():
    entities = loader.get_entities()

    return [
        {
            "source_table": entity.get("source_table"),
            "display_name": entity.get("display_name"),
            "domain": entity.get("domain"),
            "primary_key": entity.get("primary_key_source_column"),
            "dataverse_entity": entity.get("dataverse_entity_logical_name"),
            "column_count": entity.get("column_count"),
            "row_count": entity.get("row_count"),
        }
        for entity in entities
    ]


@router.get("/entities/{entity_name}")
def get_entity(entity_name: str):
    entity = loader.get_entity(entity_name)

    if not entity:
        raise HTTPException(status_code=404, detail=f"Entity not found: {entity_name}")

    return {
        "entity": entity,
        "relationships": loader.get_relationships_for_entity(entity_name),
    }


@router.get("/domains")
def get_domains():
    return loader.get_domains()


@router.get("/entity-names")
def get_entity_names():
    return loader.get_entity_names()


@router.get("/registry/{entity_name}")
def describe_entity_from_registry(entity_name: str):
    entity = registry.describe(entity_name)

    if not entity:
        raise HTTPException(status_code=404, detail=f"Entity not found: {entity_name}")

    return entity
