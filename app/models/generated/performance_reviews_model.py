from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class PerformanceReviews(BaseModel):
    performance_review_id: Optional[str] = Field(default=None, description="Performance Review Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    review_year: Optional[int] = Field(default=None, description="Review Year")
    review_cycle: Optional[str] = Field(default=None, description="Review Cycle")
    review_type: Optional[str] = Field(default=None, description="Review Type")
    overall_rating: Optional[int] = Field(default=None, description="Overall Rating")
    overall_rating_label: Optional[str] = Field(default=None, description="Overall Rating Label")
    potential_rating: Optional[str] = Field(default=None, description="Potential Rating")
    promotion_readiness: Optional[str] = Field(default=None, description="Promotion Readiness")
    gen_ai_readiness: Optional[str] = Field(default=None, description="Gen Ai Readiness")
    manager_rating: Optional[int] = Field(default=None, description="Manager Rating")
    self_rating: Optional[int] = Field(default=None, description="Self Rating")
    calibration_adjustment: Optional[str] = Field(default=None, description="Calibration Adjustment")
    review_status: Optional[str] = Field(default=None, description="Review Status")
    review_completion_date: Optional[date] = Field(default=None, description="Review Completion Date")


class PerformanceReviewsResponse(BaseModel):
    value: list[PerformanceReviews]
    count: Optional[int] = None