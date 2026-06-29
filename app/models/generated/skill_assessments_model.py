from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class SkillAssessments(BaseModel):
    assessment_id: Optional[str] = Field(default=None, description="Assessment Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    skill_id: Optional[str] = Field(default=None, description="Skill Id")
    assessment_date: Optional[date] = Field(default=None, description="Assessment Date")
    assessor_type: Optional[str] = Field(default=None, description="Assessor Type")
    previous_level: Optional[int] = Field(default=None, description="Previous Level")
    current_level: Optional[int] = Field(default=None, description="Current Level")
    assessment_method: Optional[str] = Field(
        default=None, description="Assessment Method"
    )


class SkillAssessmentsResponse(BaseModel):
    value: list[SkillAssessments]
    count: Optional[int] = None
