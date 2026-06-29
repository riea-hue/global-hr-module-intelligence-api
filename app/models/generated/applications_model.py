from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Applications(BaseModel):
    application_id: Optional[str] = Field(default=None, description="Application Id")
    candidate_id: Optional[str] = Field(default=None, description="Candidate Id")
    job_requisition_id: Optional[str] = Field(
        default=None, description="Job Requisition Id"
    )
    application_date: Optional[date] = Field(
        default=None, description="Application Date"
    )
    application_status: Optional[str] = Field(
        default=None, description="Application Status"
    )
    application_stage: Optional[str] = Field(
        default=None, description="Application Stage"
    )
    source: Optional[str] = Field(default=None, description="Source")
    candidate_type: Optional[str] = Field(default=None, description="Candidate Type")
    internal_candidate: Optional[bool] = Field(
        default=None, description="Internal Candidate"
    )
    screening_score: Optional[int] = Field(default=None, description="Screening Score")
    gen_ai_skill_match: Optional[str] = Field(
        default=None, description="Gen Ai Skill Match"
    )
    requisition_priority: Optional[str] = Field(
        default=None, description="Requisition Priority"
    )
    requisition_country: Optional[str] = Field(
        default=None, description="Requisition Country"
    )
    requisition_region: Optional[str] = Field(
        default=None, description="Requisition Region"
    )
    career_level_target: Optional[str] = Field(
        default=None, description="Career Level Target"
    )
    disposition_reason: Optional[str] = Field(
        default=None, description="Disposition Reason"
    )


class ApplicationsResponse(BaseModel):
    value: list[Applications]
    count: Optional[int] = None
