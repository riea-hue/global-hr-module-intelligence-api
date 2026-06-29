from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class PayGroups(BaseModel):
    pay_group_id: Optional[str] = Field(default=None, description="Pay Group Id")
    pay_group_name: Optional[str] = Field(default=None, description="Pay Group Name")
    country: Optional[str] = Field(default=None, description="Country")
    region: Optional[str] = Field(default=None, description="Region")
    currency: Optional[str] = Field(default=None, description="Currency")
    worker_type: Optional[str] = Field(default=None, description="Worker Type")
    pay_frequency: Optional[str] = Field(default=None, description="Pay Frequency")
    payroll_calendar_type: Optional[str] = Field(
        default=None, description="Payroll Calendar Type"
    )
    pay_periods_per_year: Optional[int] = Field(
        default=None, description="Pay Periods Per Year"
    )
    pay_day_rule: Optional[str] = Field(default=None, description="Pay Day Rule")
    payroll_provider: Optional[str] = Field(
        default=None, description="Payroll Provider"
    )
    is_active: Optional[bool] = Field(default=None, description="Is Active")


class PayGroupsResponse(BaseModel):
    value: list[PayGroups]
    count: Optional[int] = None
