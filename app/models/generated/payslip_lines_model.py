from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class PayslipLines(BaseModel):
    payslip_line_id: Optional[str] = Field(default=None, description="Payslip Line Id")
    payroll_result_id: Optional[str] = Field(
        default=None, description="Payroll Result Id"
    )
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    line_category: Optional[str] = Field(default=None, description="Line Category")
    line_name: Optional[str] = Field(default=None, description="Line Name")
    amount: Optional[float] = Field(default=None, description="Amount")
    currency: Optional[str] = Field(default=None, description="Currency")


class PayslipLinesResponse(BaseModel):
    value: list[PayslipLines]
    count: Optional[int] = None
