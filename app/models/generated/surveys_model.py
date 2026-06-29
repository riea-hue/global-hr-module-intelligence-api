from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Surveys(BaseModel):
    survey_id: Optional[str] = Field(default=None, description="Survey Id")
    survey_name: Optional[str] = Field(default=None, description="Survey Name")
    survey_type: Optional[str] = Field(default=None, description="Survey Type")
    launch_date: Optional[date] = Field(default=None, description="Launch Date")
    close_date: Optional[date] = Field(default=None, description="Close Date")
    target_population: Optional[str] = Field(
        default=None, description="Target Population"
    )
    participation_rate: Optional[float] = Field(
        default=None, description="Participation Rate"
    )


class SurveysResponse(BaseModel):
    value: list[Surveys]
    count: Optional[int] = None
