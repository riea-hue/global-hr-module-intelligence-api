from pathlib import Path

from engine.generators.metadata_loader import MetadataLoader


PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = PROJECT_ROOT / "app" / "models" / "generated"


TYPE_MAP = {
    "Edm.String": "Optional[str]",
    "Edm.Int32": "Optional[int]",
    "Edm.Int64": "Optional[int]",
    "Edm.Decimal": "Optional[float]",
    "Edm.Double": "Optional[float]",
    "Edm.Boolean": "Optional[bool]",
    "Edm.Date": "Optional[date]",
    "Edm.DateTimeOffset": "Optional[datetime]",
}


def to_class_name(source_table: str) -> str:
    return "".join(word.capitalize() for word in source_table.split("_"))


def map_type(api_type: str) -> str:
    return TYPE_MAP.get(api_type, "Optional[str]")


def generate_model(source_table: str) -> Path:
    loader = MetadataLoader()
    entity = loader.build_entity_definition(source_table)

    class_name = to_class_name(source_table)
    output_file = OUTPUT_DIR / f"{source_table}_model.py"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    lines = [
        "from datetime import date, datetime",
        "from typing import Optional",
        "from pydantic import BaseModel, Field",
        "",
        "",
        f"class {class_name}(BaseModel):",
    ]

    attributes = entity["attributes"]

    if not attributes:
        lines.append("    pass")
    else:
        for attribute in attributes:
            field_name = attribute.get("source_column") or attribute.get("logical_name")
            display_name = attribute.get("display_name", field_name)
            api_type = attribute.get("api_type", "Edm.String")
            python_type = map_type(api_type)

            lines.append(
                f'    {field_name}: {python_type} = Field(default=None, description="{display_name}")'
            )

    lines.extend(
        [
            "",
            "",
            f"class {class_name}Response(BaseModel):",
            f"    value: list[{class_name}]",
            "    count: Optional[int] = None",
        ]
    )

    output_file.write_text("\n".join(lines), encoding="utf-8")

    return output_file


if __name__ == "__main__":
    generated_file = generate_model("applications")
    print(f"Generated model: {generated_file}")
