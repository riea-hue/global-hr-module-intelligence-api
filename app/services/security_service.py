from fastapi import Header, HTTPException

from app.services.metadata_service import MetadataService
from app.services.rbac_service import RBACService


metadata_service = MetadataService()
rbac_service = RBACService()


def enforce_department_access(
    entity_name: str,
    x_department: str | None = Header(default=None, alias="X-Department"),
) -> dict:
    if not x_department:
        raise HTTPException(
            status_code=403,
            detail="Missing required header: X-Department",
        )

    try:
        entity_metadata = metadata_service.get_entity(entity_name)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    csv_file = entity_metadata.get("csv_file")

    if not rbac_service.can_access_csv(x_department, csv_file):
        raise HTTPException(
            status_code=403,
            detail={
                "message": "Access denied.",
                "department": x_department,
                "entity": entity_name,
                "csv_file": csv_file,
            },
        )

    return {
        "department": x_department,
        "entity": entity_name,
        "csv_file": csv_file,
        "authorized": True,
    }
