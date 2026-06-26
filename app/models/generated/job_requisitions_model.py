from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class JobRequisitions(BaseModel):
    job_requisition_id: Optional[str] = Field(default=None, description="Job Requisition Id")
    requisition_title: Optional[str] = Field(default=None, description="Requisition Title")
    job_profile_id: Optional[str] = Field(default=None, description="Job Profile Id")
    job_family: Optional[str] = Field(default=None, description="Job Family")
    career_level: Optional[str] = Field(default=None, description="Career Level")
    business_unit: Optional[str] = Field(default=None, description="Business Unit")
    company_id: Optional[str] = Field(default=None, description="Company Id")
    location_id: Optional[str] = Field(default=None, description="Location Id")
    country: Optional[str] = Field(default=None, description="Country")
    region: Optional[str] = Field(default=None, description="Region")
    cost_center_id: Optional[str] = Field(default=None, description="Cost Center Id")
    supervisory_org_id: Optional[str] = Field(default=None, description="Supervisory Org Id")
    hiring_manager_worker_id: Optional[str] = Field(default=None, description="Hiring Manager Worker Id")
    recruiter_worker_id: Optional[str] = Field(default=None, description="Recruiter Worker Id")
    requisition_status: Optional[str] = Field(default=None, description="Requisition Status")
    approval_status: Optional[str] = Field(default=None, description="Approval Status")
    requisition_reason: Optional[str] = Field(default=None, description="Requisition Reason")
    employment_type: Optional[str] = Field(default=None, description="Employment Type")
    worker_type: Optional[str] = Field(default=None, description="Worker Type")
    target_openings: Optional[int] = Field(default=None, description="Target Openings")
    filled_openings: Optional[int] = Field(default=None, description="Filled Openings")
    opened_date: Optional[date] = Field(default=None, description="Opened Date")
    closed_date: Optional[date] = Field(default=None, description="Closed Date")
    target_start_date: Optional[date] = Field(default=None, description="Target Start Date")
    time_to_fill_days: Optional[float] = Field(default=None, description="Time To Fill Days")
    primary_recruiting_source: Optional[str] = Field(default=None, description="Primary Recruiting Source")
    priority: Optional[str] = Field(default=None, description="Priority")
    gen_ai_critical_requisition: Optional[bool] = Field(default=None, description="Gen Ai Critical Requisition")
    confidential_requisition: Optional[bool] = Field(default=None, description="Confidential Requisition")


class JobRequisitionsResponse(BaseModel):
    value: list[JobRequisitions]
    count: Optional[int] = None