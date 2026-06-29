from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class Locations(BaseModel):
    location_id: Optional[str] = Field(default=None, description="Location Id")
    location_name: Optional[str] = Field(default=None, description="Location Name")
    company_id: Optional[str] = Field(default=None, description="Company Id")
    country: Optional[str] = Field(default=None, description="Country")
    city: Optional[str] = Field(default=None, description="City")
    region: Optional[str] = Field(default=None, description="Region")
    location_type: Optional[str] = Field(default=None, description="Location Type")


class LocationsResponse(BaseModel):
    value: list[Locations]
    count: Optional[int] = None
