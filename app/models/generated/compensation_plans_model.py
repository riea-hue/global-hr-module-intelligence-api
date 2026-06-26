from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class CompensationPlans(BaseModel):
    compensation_plan_id: Optional[str] = Field(default=None, description="Compensation Plan Id")
    plan_name: Optional[str] = Field(default=None, description="Plan Name")
    eligible_worker_type: Optional[str] = Field(default=None, description="Eligible Worker Type")
    pay_frequency: Optional[str] = Field(default=None, description="Pay Frequency")
    bonus_eligible: Optional[bool] = Field(default=None, description="Bonus Eligible")


class CompensationPlansResponse(BaseModel):
    value: list[CompensationPlans]
    count: Optional[int] = None