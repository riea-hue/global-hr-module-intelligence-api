from fastapi import APIRouter, Header, HTTPException

from app.services.metadata_service import MetadataService
from app.services.rbac_service import RBACService


router = APIRouter(prefix="/api/v1", tags=["Metadata"])

metadata_service = MetadataService()
rbac_service = RBACService()


@router.get("/entities")
def list_entities():
    return metadata_service.list_entities()


@router.get("/entities/{entity_name}/access")
def check_entity_access(
    entity_name: str,
    x_department: str | None = Header(default=None, alias="X-Department"),
):
    if not x_department:
        raise HTTPException(
            status_code=403,
            detail="Missing required header: X-Department",
        )

    try:
        entity = metadata_service.get_entity(entity_name)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    csv_file = entity.get("csv_file")
    authorized = rbac_service.can_access_csv(x_department, csv_file)

    return {
        "department": x_department,
        "entity": entity_name,
        "csv_file": csv_file,
        "authorized": authorized,
        "access_context": rbac_service.get_access_context(x_department),
    }


@router.get("/entities/{entity_name}")
def get_entity_metadata(entity_name: str):
    try:
        return metadata_service.get_entity(entity_name)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error


@router.get("/$metadata")
def get_metadata_catalog():
    return metadata_service.get_catalog()