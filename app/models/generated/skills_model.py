from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Skills(BaseModel):
    skill_id: Optional[str] = Field(default=None, description="Skill Id")
    skill_name: Optional[str] = Field(default=None, description="Skill Name")
    skill_category: Optional[str] = Field(default=None, description="Skill Category")
    skill_family: Optional[str] = Field(default=None, description="Skill Family")
    proficiency_scale: Optional[str] = Field(default=None, description="Proficiency Scale")
    emerging_skill_flag: Optional[bool] = Field(default=None, description="Emerging Skill Flag")
    gen_ai_related_flag: Optional[bool] = Field(default=None, description="Gen Ai Related Flag")
    is_active: Optional[bool] = Field(default=None, description="Is Active")


class SkillsResponse(BaseModel):
    value: list[Skills]
    count: Optional[int] = None