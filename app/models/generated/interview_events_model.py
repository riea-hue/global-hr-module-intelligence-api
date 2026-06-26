from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class InterviewEvents(BaseModel):
    interview_event_id: Optional[str] = Field(default=None, description="Interview Event Id")
    application_id: Optional[str] = Field(default=None, description="Application Id")
    candidate_id: Optional[str] = Field(default=None, description="Candidate Id")
    job_requisition_id: Optional[str] = Field(default=None, description="Job Requisition Id")
    interview_round: Optional[int] = Field(default=None, description="Interview Round")
    interview_type: Optional[str] = Field(default=None, description="Interview Type")
    interview_date: Optional[date] = Field(default=None, description="Interview Date")
    interviewer_worker_id: Optional[str] = Field(default=None, description="Interviewer Worker Id")
    interview_status: Optional[str] = Field(default=None, description="Interview Status")
    interview_score: Optional[int] = Field(default=None, description="Interview Score")
    recommendation: Optional[str] = Field(default=None, description="Recommendation")
    gen_ai_assessment_score: Optional[int] = Field(default=None, description="Gen Ai Assessment Score")


class InterviewEventsResponse(BaseModel):
    value: list[InterviewEvents]
    count: Optional[int] = None