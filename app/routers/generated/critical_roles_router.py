from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.models.generated.critical_roles_model import CriticalRoles
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(prefix="/api/v1/critical_roles", tags=["Succession Planning"])

require_access = partial(enforce_department_access, "critical_roles")


@router.get(
    "",
    summary="Get critical_roles",
    description="Generated endpoint for Global HR - Succession Planning. Owner: Talent Management. Classification: Restricted.",
)
def get_critical_roles(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("critical_roles.csv")

    try:
        result = apply_odata_query(
            df=df,
            select=select,
            filter=filter,
            orderby=orderby,
            top=top,
            skip=skip,
            count=count,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return result


@router.get(
    "/{record_id}", response_model=CriticalRoles, summary="Get critical_roles by ID"
)
def get_critical_roles_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("critical_roles.csv")
    record = df[df["critical_role_id"] == record_id]

    if record.empty:
        raise HTTPException(status_code=404, detail="critical_roles record not found")

    return record.iloc[0].to_dict()
