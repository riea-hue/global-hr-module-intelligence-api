from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class CostCenters(BaseModel):
    cost_center_id: Optional[str] = Field(default=None, description="Cost Center Id")
    cost_center_name: Optional[str] = Field(default=None, description="Cost Center Name")
    company_id: Optional[str] = Field(default=None, description="Company Id")
    business_unit: Optional[str] = Field(default=None, description="Business Unit")
    function: Optional[str] = Field(default=None, description="Function")
    is_active: Optional[bool] = Field(default=None, description="Is Active")


class CostCentersResponse(BaseModel):
    value: list[CostCenters]
    count: Optional[int] = None