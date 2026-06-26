from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class AbsencePlans(BaseModel):
    absence_plan_id: Optional[str] = Field(default=None, description="Absence Plan Id")
    absence_plan_name: Optional[str] = Field(default=None, description="Absence Plan Name")
    country: Optional[str] = Field(default=None, description="Country")
    region: Optional[str] = Field(default=None, description="Region")
    absence_type: Optional[str] = Field(default=None, description="Absence Type")
    annual_entitlement_days: Optional[int] = Field(default=None, description="Annual Entitlement Days")
    carryover_allowed: Optional[bool] = Field(default=None, description="Carryover Allowed")
    max_carryover_days: Optional[int] = Field(default=None, description="Max Carryover Days")
    requires_approval: Optional[bool] = Field(default=None, description="Requires Approval")
    is_paid_leave: Optional[bool] = Field(default=None, description="Is Paid Leave")
    active_flag: Optional[bool] = Field(default=None, description="Active Flag")


class AbsencePlansResponse(BaseModel):
    value: list[AbsencePlans]
    count: Optional[int] = None