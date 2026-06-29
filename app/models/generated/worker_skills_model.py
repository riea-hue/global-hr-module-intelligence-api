from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class WorkerSkills(BaseModel):
    worker_skill_id: Optional[str] = Field(default=None, description="Worker Skill Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    skill_id: Optional[str] = Field(default=None, description="Skill Id")
    proficiency_level: Optional[int] = Field(
        default=None, description="Proficiency Level"
    )
    source: Optional[str] = Field(default=None, description="Source")
    validated_flag: Optional[bool] = Field(default=None, description="Validated Flag")
    last_assessed_date: Optional[date] = Field(
        default=None, description="Last Assessed Date"
    )


class WorkerSkillsResponse(BaseModel):
    value: list[WorkerSkills]
    count: Optional[int] = None
