from app.metadata.metadata_loader import MetadataLoader
from app.metadata.entity_registry import EntityRegistry

metadata_loader = MetadataLoader()
entity_registry = EntityRegistry(metadata_loader)
