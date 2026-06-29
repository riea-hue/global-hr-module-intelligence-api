from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.models.generated.personal_development_plans_model import (
    PersonalDevelopmentPlans,
)
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(
    prefix="/api/v1/personal_development_plans", tags=["Personal Development Plans"]
)

require_access = partial(enforce_department_access, "personal_development_plans")


@router.get(
    "",
    summary="Get personal_development_plans",
    description="Generated endpoint for Global HR - Personal Development Plans. Owner: Talent Management. Classification: Restricted.",
)
def get_personal_development_plans(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("personal_development_plans.csv")

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
    "/{record_id}",
    response_model=PersonalDevelopmentPlans,
    summary="Get personal_development_plans by ID",
)
def get_personal_development_plans_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("personal_development_plans.csv")
    record = df[df["pdp_id"] == record_id]

    if record.empty:
        raise HTTPException(
            status_code=404, detail="personal_development_plans record not found"
        )

    return record.iloc[0].to_dict()
