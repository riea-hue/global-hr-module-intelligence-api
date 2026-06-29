from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from app.models.generated.survey_responses_model import SurveyResponses
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(prefix="/api/v1/survey_responses", tags=["Engagement Surveys"])

require_access = partial(enforce_department_access, "survey_responses")


@router.get(
    "",
    summary="Get survey_responses",
    description="Generated endpoint for Global HR - Engagement Surveys. Owner: People Analytics. Classification: Restricted.",
)
def get_survey_responses(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("survey_responses.csv")

    try:
        result = apply_odata_query(
            df=df,
            select=select,
            filter=filter,
            orderby=orderby,
            top=top,
            skip=skip,
            count=count,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return result


@router.get(
    "/{record_id}", response_model=SurveyResponses, summary="Get survey_responses by ID"
)
def get_survey_responses_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("survey_responses.csv")
    record = df[df["response_id"] == record_id]

    if record.empty:
        raise HTTPException(status_code=404, detail="survey_responses record not found")

    return record.iloc[0].to_dict()
