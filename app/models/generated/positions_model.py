from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Positions(BaseModel):
    position_id: Optional[str] = Field(default=None, description="Position Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    position_title: Optional[str] = Field(default=None, description="Position Title")
    job_profile_id: Optional[str] = Field(default=None, description="Job Profile Id")
    supervisory_org_id: Optional[str] = Field(
        default=None, description="Supervisory Org Id"
    )
    cost_center_id: Optional[str] = Field(default=None, description="Cost Center Id")
    position_status: Optional[str] = Field(default=None, description="Position Status")
    effective_start_date: Optional[date] = Field(
        default=None, description="Effective Start Date"
    )
    effective_end_date: Optional[date] = Field(
        default=None, description="Effective End Date"
    )


class PositionsResponse(BaseModel):
    value: list[Positions]
    count: Optional[int] = None
