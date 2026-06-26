from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class CompensationGrades(BaseModel):
    compensation_grade_id: Optional[str] = Field(default=None, description="Compensation Grade Id")
    global_grade: Optional[str] = Field(default=None, description="Global Grade")
    career_level: Optional[str] = Field(default=None, description="Career Level")
    job_family: Optional[str] = Field(default=None, description="Job Family")
    market_reference_zone: Optional[str] = Field(default=None, description="Market Reference Zone")
    salary_band_min: Optional[int] = Field(default=None, description="Salary Band Min")
    salary_band_mid: Optional[int] = Field(default=None, description="Salary Band Mid")
    salary_band_max: Optional[int] = Field(default=None, description="Salary Band Max")
    bonus_target: Optional[float] = Field(default=None, description="Bonus Target")
    currency: Optional[str] = Field(default=None, description="Currency")
    country: Optional[str] = Field(default=None, description="Country")
    geo_differential: Optional[float] = Field(default=None, description="Geo Differential")
    gen_ai_impact_level: Optional[str] = Field(default=None, description="Gen Ai Impact Level")
    gen_ai_skill_premium: Optional[float] = Field(default=None, description="Gen Ai Skill Premium")
    gen_ai_role_category: Optional[str] = Field(default=None, description="Gen Ai Role Category")


class CompensationGradesResponse(BaseModel):
    value: list[CompensationGrades]
    count: Optional[int] = None