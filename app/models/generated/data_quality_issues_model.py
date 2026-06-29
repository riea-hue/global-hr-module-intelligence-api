from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class DataQualityIssues(BaseModel):
    dq_issue_id: Optional[str] = Field(default=None, description="Dq Issue Id")
    issue_date: Optional[date] = Field(default=None, description="Issue Date")
    severity: Optional[str] = Field(default=None, description="Severity")
    domain: Optional[str] = Field(default=None, description="Domain")
    table_name: Optional[str] = Field(default=None, description="Table Name")
    issue_type: Optional[str] = Field(default=None, description="Issue Type")
    source_validation_id: Optional[float] = Field(
        default=None, description="Source Validation Id"
    )
    affected_record_count: Optional[int] = Field(
        default=None, description="Affected Record Count"
    )
    business_impact: Optional[str] = Field(default=None, description="Business Impact")
    status: Optional[str] = Field(default=None, description="Status")
    owner_team: Optional[str] = Field(default=None, description="Owner Team")
    remediation_due_date: Optional[date] = Field(
        default=None, description="Remediation Due Date"
    )


class DataQualityIssuesResponse(BaseModel):
    value: list[DataQualityIssues]
    count: Optional[int] = None
