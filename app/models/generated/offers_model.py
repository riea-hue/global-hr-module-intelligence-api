from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Offers(BaseModel):
    offer_id: Optional[str] = Field(default=None, description="Offer Id")
    application_id: Optional[str] = Field(default=None, description="Application Id")
    candidate_id: Optional[str] = Field(default=None, description="Candidate Id")
    job_requisition_id: Optional[str] = Field(default=None, description="Job Requisition Id")
    offer_date: Optional[date] = Field(default=None, description="Offer Date")
    offer_status: Optional[str] = Field(default=None, description="Offer Status")
    response_date: Optional[date] = Field(default=None, description="Response Date")
    expected_start_date: Optional[date] = Field(default=None, description="Expected Start Date")
    decline_reason: Optional[str] = Field(default=None, description="Decline Reason")
    offered_currency: Optional[str] = Field(default=None, description="Offered Currency")
    offered_base_pay_amount: Optional[int] = Field(default=None, description="Offered Base Pay Amount")
    offered_base_pay_frequency: Optional[str] = Field(default=None, description="Offered Base Pay Frequency")
    sign_on_bonus_amount: Optional[int] = Field(default=None, description="Sign On Bonus Amount")
    bonus_target_percentage: Optional[float] = Field(default=None, description="Bonus Target Percentage")
    compensation_grade_id: Optional[str] = Field(default=None, description="Compensation Grade Id")
    market_position_ratio: Optional[float] = Field(default=None, description="Market Position Ratio")
    salary_band_min: Optional[int] = Field(default=None, description="Salary Band Min")
    salary_band_mid: Optional[int] = Field(default=None, description="Salary Band Mid")
    salary_band_max: Optional[int] = Field(default=None, description="Salary Band Max")
    gen_ai_skill_match: Optional[str] = Field(default=None, description="Gen Ai Skill Match")
    gen_ai_premium_applied: Optional[bool] = Field(default=None, description="Gen Ai Premium Applied")
    gen_ai_premium_amount: Optional[int] = Field(default=None, description="Gen Ai Premium Amount")
    avg_interview_score: Optional[float] = Field(default=None, description="Avg Interview Score")
    avg_gen_ai_assessment_score: Optional[float] = Field(default=None, description="Avg Gen Ai Assessment Score")
    final_recommendation: Optional[str] = Field(default=None, description="Final Recommendation")
    completed_interview_count: Optional[int] = Field(default=None, description="Completed Interview Count")


class OffersResponse(BaseModel):
    value: list[Offers]
    count: Optional[int] = None