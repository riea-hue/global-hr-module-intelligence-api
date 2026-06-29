from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class SurveyResponses(BaseModel):
    response_id: Optional[str] = Field(default=None, description="Response Id")
    survey_id: Optional[str] = Field(default=None, description="Survey Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    question_category: Optional[str] = Field(
        default=None, description="Question Category"
    )
    score: Optional[int] = Field(default=None, description="Score")
    sentiment: Optional[str] = Field(default=None, description="Sentiment")
    submitted_date: Optional[date] = Field(default=None, description="Submitted Date")


class SurveyResponsesResponse(BaseModel):
    value: list[SurveyResponses]
    count: Optional[int] = None
