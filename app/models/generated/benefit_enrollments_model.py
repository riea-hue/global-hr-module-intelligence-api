from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class BenefitEnrollments(BaseModel):
    benefit_enrollment_id: Optional[str] = Field(
        default=None, description="Benefit Enrollment Id"
    )
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    benefit_plan_id: Optional[str] = Field(default=None, description="Benefit Plan Id")
    benefit_type: Optional[str] = Field(default=None, description="Benefit Type")
    country: Optional[str] = Field(default=None, description="Country")
    region: Optional[str] = Field(default=None, description="Region")
    coverage_level: Optional[str] = Field(default=None, description="Coverage Level")
    enrollment_status: Optional[str] = Field(
        default=None, description="Enrollment Status"
    )
    effective_date: Optional[date] = Field(default=None, description="Effective Date")
    end_date: Optional[date] = Field(default=None, description="End Date")
    employee_contribution_pct: Optional[float] = Field(
        default=None, description="Employee Contribution Pct"
    )
    employer_contribution_pct: Optional[float] = Field(
        default=None, description="Employer Contribution Pct"
    )


class BenefitEnrollmentsResponse(BaseModel):
    value: list[BenefitEnrollments]
    count: Optional[int] = None
