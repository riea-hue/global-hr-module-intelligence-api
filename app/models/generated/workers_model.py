from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Workers(BaseModel):
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    employee_id: Optional[str] = Field(default=None, description="Employee Id")
    first_name: Optional[str] = Field(default=None, description="First Name")
    last_name: Optional[str] = Field(default=None, description="Last Name")
    work_email: Optional[str] = Field(default=None, description="Work Email")
    date_of_birth: Optional[str] = Field(default=None, description="Date Of Birth")
    gender: Optional[str] = Field(default=None, description="Gender")
    worker_type: Optional[str] = Field(default=None, description="Worker Type")
    worker_status: Optional[str] = Field(default=None, description="Worker Status")
    hire_date: Optional[date] = Field(default=None, description="Hire Date")
    termination_date: Optional[date] = Field(
        default=None, description="Termination Date"
    )
    company_id: Optional[str] = Field(default=None, description="Company Id")
    location_id: Optional[str] = Field(default=None, description="Location Id")
    job_profile_id: Optional[str] = Field(default=None, description="Job Profile Id")
    supervisory_org_id: Optional[str] = Field(
        default=None, description="Supervisory Org Id"
    )


class WorkersResponse(BaseModel):
    value: list[Workers]
    count: Optional[int] = None
