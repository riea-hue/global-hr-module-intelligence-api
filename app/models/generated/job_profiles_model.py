from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class JobProfiles(BaseModel):
    job_profile_id: Optional[str] = Field(default=None, description="Job Profile Id")
    job_profile_name: Optional[str] = Field(
        default=None, description="Job Profile Name"
    )
    job_family_id: Optional[str] = Field(default=None, description="Job Family Id")
    job_level: Optional[str] = Field(default=None, description="Job Level")
    exempt_status: Optional[str] = Field(default=None, description="Exempt Status")
    is_people_manager_role: Optional[bool] = Field(
        default=None, description="Is People Manager Role"
    )


class JobProfilesResponse(BaseModel):
    value: list[JobProfiles]
    count: Optional[int] = None
