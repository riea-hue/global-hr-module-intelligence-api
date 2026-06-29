from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class SupervisoryOrganizations(BaseModel):
    supervisory_org_id: Optional[str] = Field(
        default=None, description="Supervisory Org Id"
    )
    supervisory_org_name: Optional[str] = Field(
        default=None, description="Supervisory Org Name"
    )
    parent_supervisory_org_id: Optional[str] = Field(
        default=None, description="Parent Supervisory Org Id"
    )
    company_id: Optional[str] = Field(default=None, description="Company Id")
    cost_center_id: Optional[str] = Field(default=None, description="Cost Center Id")
    business_unit: Optional[str] = Field(default=None, description="Business Unit")


class SupervisoryOrganizationsResponse(BaseModel):
    value: list[SupervisoryOrganizations]
    count: Optional[int] = None
