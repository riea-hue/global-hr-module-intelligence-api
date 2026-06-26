from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.models.generated.positions_model import Positions
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(
    prefix="/api/v1/positions",
    tags=["Core HR / Organization"]
)

require_access = partial(enforce_department_access, "positions")


@router.get(
    "",
    summary="Get positions",
    description="Generated endpoint for Global HR - Core HR / Organization. Owner: HRIS / Core HR. Classification: Confidential."
)
def get_positions(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("positions.csv")

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
    response_model=Positions,
    summary="Get positions by ID"
)
def get_positions_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("positions.csv")
    record = df[df["position_id"] == record_id]

    if record.empty:
        raise HTTPException(
            status_code=404,
            detail="positions record not found"
        )

    return record.iloc[0].to_dict()
