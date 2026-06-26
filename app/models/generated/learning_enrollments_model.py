from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class LearningEnrollments(BaseModel):
    learning_enrollment_id: Optional[str] = Field(default=None, description="Learning Enrollment Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    learning_course_id: Optional[str] = Field(default=None, description="Learning Course Id")
    pdp_id: Optional[str] = Field(default=None, description="Pdp Id")
    goal_id: Optional[str] = Field(default=None, description="Goal Id")
    enrollment_source: Optional[str] = Field(default=None, description="Enrollment Source")
    enrollment_date: Optional[date] = Field(default=None, description="Enrollment Date")
    completion_date: Optional[date] = Field(default=None, description="Completion Date")
    enrollment_status: Optional[str] = Field(default=None, description="Enrollment Status")
    completion_percentage: Optional[int] = Field(default=None, description="Completion Percentage")
    learning_hours_completed: Optional[float] = Field(default=None, description="Learning Hours Completed")
    course_score: Optional[float] = Field(default=None, description="Course Score")
    certification_earned: Optional[bool] = Field(default=None, description="Certification Earned")
    course_category: Optional[str] = Field(default=None, description="Course Category")
    development_focus_area: Optional[str] = Field(default=None, description="Development Focus Area")
    gen_ai_related: Optional[bool] = Field(default=None, description="Gen Ai Related")


class LearningEnrollmentsResponse(BaseModel):
    value: list[LearningEnrollments]
    count: Optional[int] = None