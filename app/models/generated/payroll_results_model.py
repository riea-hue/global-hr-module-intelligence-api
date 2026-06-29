from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field


class PayrollResults(BaseModel):
    payroll_result_id: Optional[str] = Field(
        default=None, description="Payroll Result Id"
    )
    worker_id: Optional[str] = Field(default=None, description="Worker Id")
    pay_group_id: Optional[str] = Field(default=None, description="Pay Group Id")
    pay_period_start: Optional[str] = Field(
        default=None, description="Pay Period Start"
    )
    pay_period_end: Optional[str] = Field(default=None, description="Pay Period End")
    pay_date: Optional[date] = Field(default=None, description="Pay Date")
    currency: Optional[str] = Field(default=None, description="Currency")
    gross_pay: Optional[float] = Field(default=None, description="Gross Pay")
    base_pay: Optional[float] = Field(default=None, description="Base Pay")
    bonus_pay: Optional[float] = Field(default=None, description="Bonus Pay")
    overtime_pay: Optional[float] = Field(default=None, description="Overtime Pay")
    allowances: Optional[float] = Field(default=None, description="Allowances")
    deductions: Optional[float] = Field(default=None, description="Deductions")
    tax_withholding: Optional[float] = Field(
        default=None, description="Tax Withholding"
    )
    net_pay: Optional[float] = Field(default=None, description="Net Pay")
    pay_frequency: Optional[str] = Field(default=None, description="Pay Frequency")
    payroll_status: Optional[str] = Field(default=None, description="Payroll Status")
    gen_ai_premium_applied: Optional[bool] = Field(
        default=None, description="Gen Ai Premium Applied"
    )
    gen_ai_impact_level: Optional[str] = Field(
        default=None, description="Gen Ai Impact Level"
    )


class PayrollResultsResponse(BaseModel):
    value: list[PayrollResults]
    count: Optional[int] = None
