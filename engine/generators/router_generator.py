from pathlib import Path

from engine.generators.metadata_loader import MetadataLoader
from engine.generators.model_generator import to_class_name


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "app" / "routers" / "generated"


def generate_router(source_table: str) -> Path:
    loader = MetadataLoader()
    entity = loader.build_entity_definition(source_table)

    class_name = to_class_name(source_table)
    model_module = f"app.models.generated.{source_table}_model"
    output_file = OUTPUT_DIR / f"{source_table}_router.py"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    tag_name = entity["domain"]
    csv_file = entity["csv_file"]
    primary_key = entity["primary_key"]
    data_product_name = entity["data_product_name"] or source_table
    owner_team = entity["owner_team"]
    classification = entity["classification"]

    content = f'''from functools import partial
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query

from {model_module} import {class_name}
from app.services.csv_service import load_csv_data
from app.services.odata_service import apply_odata_query
from app.services.security_service import enforce_department_access


router = APIRouter(
    prefix="/api/v1/{source_table}",
    tags=["{tag_name}"]
)

require_access = partial(enforce_department_access, "{source_table}")


@router.get(
    "",
    summary="Get {source_table}",
    description="Generated endpoint for {data_product_name}. Owner: {owner_team}. Classification: {classification}."
)
def get_{source_table}(
    select: Optional[str] = Query(default=None, alias="$select"),
    filter: Optional[str] = Query(default=None, alias="$filter"),
    orderby: Optional[str] = Query(default=None, alias="$orderby"),
    top: Optional[int] = Query(default=100, alias="$top"),
    skip: Optional[int] = Query(default=0, alias="$skip"),
    count: Optional[bool] = Query(default=False, alias="$count"),
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("{csv_file}")

    try:
        result = apply_odata_query(
            df=df,
            select=select,
            filter=filter,
            orderby=orderby,
            top=top,
            skip=skip,
            count=count
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return result


@router.get(
    "/{{record_id}}",
    response_model={class_name},
    summary="Get {source_table} by ID"
)
def get_{source_table}_by_id(
    record_id: str,
    access_context: dict = Depends(require_access),
):
    df = load_csv_data("{csv_file}")
    record = df[df["{primary_key}"] == record_id]

    if record.empty:
        raise HTTPException(
            status_code=404,
            detail="{source_table} record not found"
        )

    return record.iloc[0].to_dict()
'''

    output_file.write_text(content, encoding="utf-8")

    return output_file


if __name__ == "__main__":
    generated_file = generate_router("applications")
    print(f"Generated router: {generated_file}")
