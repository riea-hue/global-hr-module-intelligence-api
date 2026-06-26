from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.models.generated.validation_report_model import ValidationReport
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(
    prefix="/api/v1/validation_report",
    tags=["Governance & Audit"]
)

require_access = partial(enforce_department_access, "validation_report")


@router.get(
    "",
    summary="Get validation_report",
    description="Generated endpoint for Global HR - Governance & Audit. Owner: HR Data Governance. Classification: Confidential."
)
def get_validation_report(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("validation_report.csv")

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
    response_model=ValidationReport,
    summary="Get validation_report by ID"
)
def get_validation_report_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("validation_report.csv")
    record = df[df["validation_id"] == record_id]

    if record.empty:
        raise HTTPException(
            status_code=404,
            detail="validation_report record not found"
        )

    return record.iloc[0].to_dict()
