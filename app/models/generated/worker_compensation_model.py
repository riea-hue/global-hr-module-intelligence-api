from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class WorkerCompensation(BaseModel):
    worker_compensation_id: Optional[str] = Field(default=None, description="Worker Compensation Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    effective_date: Optional[date] = Field(default=None, description="Effective Date")
    pay_currency: Optional[str] = Field(default=None, description="Pay Currency")
    base_pay_amount: Optional[float] = Field(default=None, description="Base Pay Amount")
    base_pay_frequency: Optional[str] = Field(default=None, description="Base Pay Frequency")
    bonus_target_percentage: Optional[float] = Field(default=None, description="Bonus Target Percentage")
    compensation_grade_id: Optional[str] = Field(default=None, description="Compensation Grade Id")
    compensation_plan_id: Optional[str] = Field(default=None, description="Compensation Plan Id")
    market_position_ratio: Optional[float] = Field(default=None, description="Market Position Ratio")
    compa_ratio: Optional[float] = Field(default=None, description="Compa Ratio")
    salary_band_min: Optional[int] = Field(default=None, description="Salary Band Min")
    salary_band_mid: Optional[int] = Field(default=None, description="Salary Band Mid")
    salary_band_max: Optional[int] = Field(default=None, description="Salary Band Max")
    gen_ai_impact_level: Optional[str] = Field(default=None, description="Gen Ai Impact Level")
    gen_ai_skill_premium: Optional[float] = Field(default=None, description="Gen Ai Skill Premium")
    gen_ai_premium_applied: Optional[bool] = Field(default=None, description="Gen Ai Premium Applied")
    gen_ai_premium_amount: Optional[int] = Field(default=None, description="Gen Ai Premium Amount")
    gen_ai_role_category: Optional[str] = Field(default=None, description="Gen Ai Role Category")


class WorkerCompensationResponse(BaseModel):
    value: list[WorkerCompensation]
    count: Optional[int] = None