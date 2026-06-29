from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.models.generated.benefit_plans_model import BenefitPlans
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(prefix="/api/v1/benefit_plans", tags=["Benefits"])

require_access = partial(enforce_department_access, "benefit_plans")


@router.get(
    "",
    summary="Get benefit_plans",
    description="Generated endpoint for Global HR - Benefits. Owner: Benefits COE. Classification: Confidential.",
)
def get_benefit_plans(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("benefit_plans.csv")

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
    "/{record_id}", response_model=BenefitPlans, summary="Get benefit_plans by ID"
)
def get_benefit_plans_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("benefit_plans.csv")
    record = df[df["benefit_plan_id"] == record_id]

    if record.empty:
        raise HTTPException(status_code=404, detail="benefit_plans record not found")

    return record.iloc[0].to_dict()
