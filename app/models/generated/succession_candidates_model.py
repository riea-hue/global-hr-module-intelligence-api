from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class SuccessionCandidates(BaseModel):
    succession_candidate_id: Optional[str] = Field(default=None, description="Succession Candidate Id")
    pool_id: Optional[str] = Field(default=None, description="Pool Id")
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    readiness: Optional[str] = Field(default=None, description="Readiness")
    risk_of_loss: Optional[str] = Field(default=None, description="Risk Of Loss")
    potential_rating: Optional[str] = Field(default=None, description="Potential Rating")
    performance_rating: Optional[str] = Field(default=None, description="Performance Rating")
    succession_rank: Optional[int] = Field(default=None, description="Succession Rank")
    development_need: Optional[str] = Field(default=None, description="Development Need")
    mobility_preference: Optional[str] = Field(default=None, description="Mobility Preference")
    last_reviewed_date: Optional[date] = Field(default=None, description="Last Reviewed Date")
    active_candidate_flag: Optional[bool] = Field(default=None, description="Active Candidate Flag")


class SuccessionCandidatesResponse(BaseModel):
    value: list[SuccessionCandidates]
    count: Optional[int] = None