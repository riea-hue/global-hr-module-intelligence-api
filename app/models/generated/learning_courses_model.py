from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class LearningCourses(BaseModel):
    learning_course_id: Optional[str] = Field(default=None, description="Learning Course Id")
    course_code: Optional[str] = Field(default=None, description="Course Code")
    course_title: Optional[str] = Field(default=None, description="Course Title")
    course_category: Optional[str] = Field(default=None, description="Course Category")
    development_focus_area: Optional[str] = Field(default=None, description="Development Focus Area")
    proficiency_level: Optional[str] = Field(default=None, description="Proficiency Level")
    delivery_method: Optional[str] = Field(default=None, description="Delivery Method")
    provider: Optional[str] = Field(default=None, description="Provider")
    duration_hours: Optional[int] = Field(default=None, description="Duration Hours")
    is_mandatory: Optional[bool] = Field(default=None, description="Is Mandatory")
    certification_eligible: Optional[bool] = Field(default=None, description="Certification Eligible")
    gen_ai_related: Optional[bool] = Field(default=None, description="Gen Ai Related")
    course_status: Optional[str] = Field(default=None, description="Course Status")
    course_description: Optional[str] = Field(default=None, description="Course Description")


class LearningCoursesResponse(BaseModel):
    value: list[LearningCourses]
    count: Optional[int] = None