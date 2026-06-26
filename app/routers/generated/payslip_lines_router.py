from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.models.generated.payslip_lines_model import PayslipLines
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(
    prefix="/api/v1/payslip_lines",
    tags=["Payroll"]
)

require_access = partial(enforce_department_access, "payslip_lines")


@router.get(
    "",
    summary="Get payslip_lines",
    description="Generated endpoint for Global HR - Payroll. Owner: Payroll Operations. Classification: Restricted."
)
def get_payslip_lines(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("payslip_lines.csv")

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
    response_model=PayslipLines,
    summary="Get payslip_lines by ID"
)
def get_payslip_lines_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("payslip_lines.csv")
    record = df[df["payslip_line_id"] == record_id]

    if record.empty:
        raise HTTPException(
            status_code=404,
            detail="payslip_lines record not found"
        )

    return record.iloc[0].to_dict()
