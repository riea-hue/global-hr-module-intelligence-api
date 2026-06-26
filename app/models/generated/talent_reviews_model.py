from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class TalentReviews(BaseModel):
    talent_review_id: Optional[str] = Field(default=None, description="Talent Review Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    performance_review_id: Optional[str] = Field(default=None, description="Performance Review Id")
    review_year: Optional[int] = Field(default=None, description="Review Year")
    performance_category: Optional[str] = Field(default=None, description="Performance Category")
    potential_category: Optional[str] = Field(default=None, description="Potential Category")
    nine_box_position: Optional[str] = Field(default=None, description="Nine Box Position")
    promotion_readiness: Optional[str] = Field(default=None, description="Promotion Readiness")
    succession_candidate: Optional[bool] = Field(default=None, description="Succession Candidate")
    ready_now_successor: Optional[bool] = Field(default=None, description="Ready Now Successor")
    critical_role: Optional[bool] = Field(default=None, description="Critical Role")
    retention_risk: Optional[str] = Field(default=None, description="Retention Risk")
    flight_risk: Optional[str] = Field(default=None, description="Flight Risk")
    promotion_count_to_date: Optional[int] = Field(default=None, description="Promotion Count To Date")
    promotion_velocity: Optional[str] = Field(default=None, description="Promotion Velocity")
    recent_manager_changes: Optional[int] = Field(default=None, description="Recent Manager Changes")
    compa_ratio: Optional[float] = Field(default=None, description="Compa Ratio")
    gen_ai_impact_level: Optional[str] = Field(default=None, description="Gen Ai Impact Level")
    gen_ai_role_category: Optional[str] = Field(default=None, description="Gen Ai Role Category")
    gen_ai_premium_applied: Optional[bool] = Field(default=None, description="Gen Ai Premium Applied")
    completed_learning_count: Optional[int] = Field(default=None, description="Completed Learning Count")
    gen_ai_learning_count: Optional[int] = Field(default=None, description="Gen Ai Learning Count")
    certifications_earned: Optional[int] = Field(default=None, description="Certifications Earned")
    learning_hours_completed: Optional[float] = Field(default=None, description="Learning Hours Completed")
    completed_pdp_count: Optional[int] = Field(default=None, description="Completed Pdp Count")
    active_pdp_count: Optional[int] = Field(default=None, description="Active Pdp Count")
    ai_focused_pdp_count: Optional[int] = Field(default=None, description="Ai Focused Pdp Count")


class TalentReviewsResponse(BaseModel):
    value: list[TalentReviews]
    count: Optional[int] = None