from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class AbsenceRequests(BaseModel):
    absence_request_id: Optional[str] = Field(
        default=None, description="Absence Request Id"
    )
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    absence_plan_id: Optional[str] = Field(default=None, description="Absence Plan Id")
    absence_type: Optional[str] = Field(default=None, description="Absence Type")
    request_date: Optional[date] = Field(default=None, description="Request Date")
    absence_start_date: Optional[date] = Field(
        default=None, description="Absence Start Date"
    )
    absence_end_date: Optional[date] = Field(
        default=None, description="Absence End Date"
    )
    duration_days: Optional[int] = Field(default=None, description="Duration Days")
    approval_status: Optional[str] = Field(default=None, description="Approval Status")
    is_paid_leave: Optional[bool] = Field(default=None, description="Is Paid Leave")


class AbsenceRequestsResponse(BaseModel):
    value: list[AbsenceRequests]
    count: Optional[int] = None
