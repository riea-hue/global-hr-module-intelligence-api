from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class CriticalRoles(BaseModel):
    critical_role_id: Optional[str] = Field(default=None, description="Critical Role Id")
    position_id: Optional[str] = Field(default=None, description="Position Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    position_title: Optional[str] = Field(default=None, description="Position Title")
    job_profile_id: Optional[str] = Field(default=None, description="Job Profile Id")
    supervisory_org_id: Optional[str] = Field(default=None, description="Supervisory Org Id")
    cost_center_id: Optional[str] = Field(default=None, description="Cost Center Id")
    criticality_level: Optional[str] = Field(default=None, description="Criticality Level")
    business_impact: Optional[str] = Field(default=None, description="Business Impact")
    succession_required_flag: Optional[bool] = Field(default=None, description="Succession Required Flag")
    risk_if_vacant: Optional[str] = Field(default=None, description="Risk If Vacant")
    target_successor_count: Optional[int] = Field(default=None, description="Target Successor Count")
    review_cycle: Optional[str] = Field(default=None, description="Review Cycle")


class CriticalRolesResponse(BaseModel):
    value: list[CriticalRoles]
    count: Optional[int] = None