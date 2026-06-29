from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class SuccessionPools(BaseModel):
    pool_id: Optional[str] = Field(default=None, description="Pool Id")
    pool_name: Optional[str] = Field(default=None, description="Pool Name")
    business_unit: Optional[str] = Field(default=None, description="Business Unit")
    pool_type: Optional[str] = Field(default=None, description="Pool Type")
    created_date: Optional[date] = Field(default=None, description="Created Date")
    pool_status: Optional[str] = Field(default=None, description="Pool Status")


class SuccessionPoolsResponse(BaseModel):
    value: list[SuccessionPools]
    count: Optional[int] = None
