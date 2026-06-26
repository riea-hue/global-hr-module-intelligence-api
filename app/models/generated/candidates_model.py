from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Candidates(BaseModel):
    candidate_id: Optional[str] = Field(default=None, description="Candidate Id")
    first_name: Optional[str] = Field(default=None, description="First Name")
    last_name: Optional[str] = Field(default=None, description="Last Name")
    candidate_email: Optional[str] = Field(default=None, description="Candidate Email")
    candidate_type: Optional[str] = Field(default=None, description="Candidate Type")
    candidate_status: Optional[str] = Field(default=None, description="Candidate Status")
    source: Optional[str] = Field(default=None, description="Source")
    country: Optional[str] = Field(default=None, description="Country")
    region: Optional[str] = Field(default=None, description="Region")
    career_level_target: Optional[str] = Field(default=None, description="Career Level Target")
    years_experience: Optional[int] = Field(default=None, description="Years Experience")
    education_level: Optional[str] = Field(default=None, description="Education Level")
    gen_ai_skill_signal: Optional[str] = Field(default=None, description="Gen Ai Skill Signal")
    willing_to_relocate: Optional[bool] = Field(default=None, description="Willing To Relocate")
    requires_work_authorization: Optional[bool] = Field(default=None, description="Requires Work Authorization")
    created_date: Optional[date] = Field(default=None, description="Created Date")
    last_activity_date: Optional[date] = Field(default=None, description="Last Activity Date")
    candidate_consent: Optional[bool] = Field(default=None, description="Candidate Consent")


class CandidatesResponse(BaseModel):
    value: list[Candidates]
    count: Optional[int] = None