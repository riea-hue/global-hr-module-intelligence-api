from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.models.generated.data_quality_issues_model import DataQualityIssues
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(
    prefix="/api/v1/data_quality_issues",
    tags=["Governance & Audit"]
)

require_access = partial(enforce_department_access, "data_quality_issues")


@router.get(
    "",
    summary="Get data_quality_issues",
    description="Generated endpoint for Global HR - Governance & Audit. Owner: HR Data Governance. Classification: Confidential."
)
def get_data_quality_issues(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("data_quality_issues.csv")

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
    response_model=DataQualityIssues,
    summary="Get data_quality_issues by ID"
)
def get_data_quality_issues_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("data_quality_issues.csv")
    record = df[df["dq_issue_id"] == record_id]

    if record.empty:
        raise HTTPException(
            status_code=404,
            detail="data_quality_issues record not found"
        )

    return record.iloc[0].to_dict()
