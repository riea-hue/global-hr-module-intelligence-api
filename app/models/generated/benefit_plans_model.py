from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class BenefitPlans(BaseModel):
    benefit_plan_id: Optional[str] = Field(default=None, description="Benefit Plan Id")
    benefit_plan_name: Optional[str] = Field(
        default=None, description="Benefit Plan Name"
    )
    country: Optional[str] = Field(default=None, description="Country")
    region: Optional[str] = Field(default=None, description="Region")
    benefit_type: Optional[str] = Field(default=None, description="Benefit Type")
    provider_name: Optional[str] = Field(default=None, description="Provider Name")
    employee_contribution_pct: Optional[float] = Field(
        default=None, description="Employee Contribution Pct"
    )
    employer_contribution_pct: Optional[float] = Field(
        default=None, description="Employer Contribution Pct"
    )
    coverage_level: Optional[str] = Field(default=None, description="Coverage Level")
    active_flag: Optional[bool] = Field(default=None, description="Active Flag")


class BenefitPlansResponse(BaseModel):
    value: list[BenefitPlans]
    count: Optional[int] = None
