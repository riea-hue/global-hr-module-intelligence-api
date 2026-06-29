from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Companies(BaseModel):
    company_id: Optional[str] = Field(default=None, description="Company Id")
    company_name: Optional[str] = Field(default=None, description="Company Name")
    country: Optional[str] = Field(default=None, description="Country")
    region: Optional[str] = Field(default=None, description="Region")
    currency: Optional[str] = Field(default=None, description="Currency")
    is_active: Optional[bool] = Field(default=None, description="Is Active")


class CompaniesResponse(BaseModel):
    value: list[Companies]
    count: Optional[int] = None
