from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class PersonalDevelopmentPlans(BaseModel):
    pdp_id: Optional[str] = Field(default=None, description="Pdp Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    performance_review_id: Optional[str] = Field(
        default=None, description="Performance Review Id"
    )
    plan_year: Optional[int] = Field(default=None, description="Plan Year")
    plan_status: Optional[str] = Field(default=None, description="Plan Status")
    career_aspiration: Optional[str] = Field(
        default=None, description="Career Aspiration"
    )
    development_focus_area: Optional[str] = Field(
        default=None, description="Development Focus Area"
    )
    development_method: Optional[str] = Field(
        default=None, description="Development Method"
    )
    promotion_readiness_target: Optional[str] = Field(
        default=None, description="Promotion Readiness Target"
    )
    mentor_assigned_worker_id: Optional[str] = Field(
        default=None, description="Mentor Assigned Worker Id"
    )
    creation_date: Optional[date] = Field(default=None, description="Creation Date")
    target_completion_date: Optional[date] = Field(
        default=None, description="Target Completion Date"
    )
    completion_percentage: Optional[int] = Field(
        default=None, description="Completion Percentage"
    )
    linked_overall_rating: Optional[int] = Field(
        default=None, description="Linked Overall Rating"
    )
    linked_potential_rating: Optional[str] = Field(
        default=None, description="Linked Potential Rating"
    )
    linked_gen_ai_readiness: Optional[str] = Field(
        default=None, description="Linked Gen Ai Readiness"
    )
    gen_ai_impact_level: Optional[str] = Field(
        default=None, description="Gen Ai Impact Level"
    )
    gen_ai_role_category: Optional[str] = Field(
        default=None, description="Gen Ai Role Category"
    )


class PersonalDevelopmentPlansResponse(BaseModel):
    value: list[PersonalDevelopmentPlans]
    count: Optional[int] = None
