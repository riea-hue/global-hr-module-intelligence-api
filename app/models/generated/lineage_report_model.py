from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class LineageReport(BaseModel):
    lineage_id: Optional[str] = Field(default=None, description="Lineage Id")
    run_timestamp: Optional[str] = Field(default=None, description="Run Timestamp")
    source_table: Optional[str] = Field(default=None, description="Source Table")
    target_table: Optional[str] = Field(default=None, description="Target Table")
    join_key_or_logic: Optional[str] = Field(default=None, description="Join Key Or Logic")
    domain: Optional[str] = Field(default=None, description="Domain")
    lineage_type: Optional[str] = Field(default=None, description="Lineage Type")
    transformation_description: Optional[str] = Field(default=None, description="Transformation Description")
    criticality: Optional[str] = Field(default=None, description="Criticality")
    active_flag: Optional[bool] = Field(default=None, description="Active Flag")


class LineageReportResponse(BaseModel):
    value: list[LineageReport]
    count: Optional[int] = None