from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class BusinessProcessEvents(BaseModel):
    business_process_event_id: Optional[str] = Field(
        default=None, description="Business Process Event Id"
    )
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    event_sequence: Optional[int] = Field(default=None, description="Event Sequence")
    event_type: Optional[str] = Field(default=None, description="Event Type")
    data_change_reason: Optional[str] = Field(
        default=None, description="Data Change Reason"
    )
    event_date: Optional[date] = Field(default=None, description="Event Date")
    effective_date: Optional[date] = Field(default=None, description="Effective Date")
    position_id: Optional[str] = Field(default=None, description="Position Id")
    supervisory_org_id: Optional[str] = Field(
        default=None, description="Supervisory Org Id"
    )
    event_status: Optional[str] = Field(default=None, description="Event Status")
    initiated_by_worker_id: Optional[str] = Field(
        default=None, description="Initiated By Worker Id"
    )


class BusinessProcessEventsResponse(BaseModel):
    value: list[BusinessProcessEvents]
    count: Optional[int] = None
