from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Goals(BaseModel):
    goal_id: Optional[str] = Field(default=None, description="Goal Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    performance_review_id: Optional[str] = Field(default=None, description="Performance Review Id")
    goal_year: Optional[int] = Field(default=None, description="Goal Year")
    goal_sequence: Optional[int] = Field(default=None, description="Goal Sequence")
    goal_category: Optional[str] = Field(default=None, description="Goal Category")
    goal_title: Optional[str] = Field(default=None, description="Goal Title")
    goal_weight: Optional[int] = Field(default=None, description="Goal Weight")
    goal_status: Optional[str] = Field(default=None, description="Goal Status")
    completion_percentage: Optional[int] = Field(default=None, description="Completion Percentage")
    goal_start_date: Optional[date] = Field(default=None, description="Goal Start Date")
    target_completion_date: Optional[date] = Field(default=None, description="Target Completion Date")
    linked_overall_rating: Optional[int] = Field(default=None, description="Linked Overall Rating")
    linked_gen_ai_readiness: Optional[str] = Field(default=None, description="Linked Gen Ai Readiness")
    gen_ai_impact_level: Optional[str] = Field(default=None, description="Gen Ai Impact Level")
    gen_ai_role_category: Optional[str] = Field(default=None, description="Gen Ai Role Category")


class GoalsResponse(BaseModel):
    value: list[Goals]
    count: Optional[int] = None