from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.models.generated.cost_centers_model import CostCenters
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(
    prefix="/api/v1/cost_centers",
    tags=["Core HR / Organization"]
)

require_access = partial(enforce_department_access, "cost_centers")


@router.get(
    "",
    summary="Get cost_centers",
    description="Generated endpoint for Global HR - Core HR / Organization. Owner: HRIS / Core HR. Classification: Restricted."
)
def get_cost_centers(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("cost_centers.csv")

    try:
        result = apply_odata_query(
            df=df,
            select=select,
            filter=filter,
            orderby=orderby,
            top=top,
            skip=skip,
            count=count
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return result


@router.get(
    "/{record_id}",
    response_model=CostCenters,
    summary="Get cost_centers by ID"
)
def get_cost_centers_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("cost_centers.csv")
    record = df[df["cost_center_id"] == record_id]

    if record.empty:
        raise HTTPException(
            status_code=404,
            detail="cost_centers record not found"
        )

    return record.iloc[0].to_dict()
