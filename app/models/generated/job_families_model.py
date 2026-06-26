from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class JobFamilies(BaseModel):
    job_family_id: Optional[str] = Field(default=None, description="Job Family Id")
    job_family_name: Optional[str] = Field(default=None, description="Job Family Name")
    business_unit: Optional[str] = Field(default=None, description="Business Unit")
    is_active: Optional[bool] = Field(default=None, description="Is Active")


class JobFamiliesResponse(BaseModel):
    value: list[JobFamilies]
    count: Optional[int] = None