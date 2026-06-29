from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class ValidationReport(BaseModel):
    validation_id: Optional[str] = Field(default=None, description="Validation Id")
    run_timestamp: Optional[str] = Field(default=None, description="Run Timestamp")
    validation_area: Optional[str] = Field(default=None, description="Validation Area")
    severity: Optional[str] = Field(default=None, description="Severity")
    table_name: Optional[str] = Field(default=None, description="Table Name")
    rule_name: Optional[str] = Field(default=None, description="Rule Name")
    records_checked: Optional[int] = Field(default=None, description="Records Checked")
    records_failed: Optional[int] = Field(default=None, description="Records Failed")
    validation_result: Optional[str] = Field(
        default=None, description="Validation Result"
    )


class ValidationReportResponse(BaseModel):
    value: list[ValidationReport]
    count: Optional[int] = None
