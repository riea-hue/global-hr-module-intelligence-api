import argparse
import importlib
import sys
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "app" / "models" / "generated"
ROUTERS_DIR = BASE_DIR / "app" / "routers" / "generated"

sys.path.insert(0, str(BASE_DIR))

from engine.generators.metadata_loader import MetadataLoader  # noqa: E402


def get_all_entities() -> list[str]:
    loader = MetadataLoader()
    resources = loader.api_catalog.get("resources", [])

    entities = [
        resource.get("source_table")
        for resource in resources
        if resource.get("source_table")
    ]

    return sorted(set(entities))


def validate_metadata(entity_name: str) -> dict:
    loader = MetadataLoader()
    entity = loader.build_entity_definition(entity_name)

    required_fields = [
        "source_table",
        "csv_file",
        "primary_key",
        "attributes",
        "domain",
    ]

    missing_fields = [
        field for field in required_fields
        if entity.get(field) in [None, "", []]
    ]

    if missing_fields:
        raise ValueError(
            f"Metadata missing required fields for {entity_name}: {missing_fields}"
        )

    return entity


def validate_csv(entity_name: str, csv_file: str, primary_key: str) -> None:
    csv_path = DATA_DIR / csv_file

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found for {entity_name}: {csv_path}")

    df = pd.read_csv(csv_path, nrows=5)

    if primary_key not in df.columns:
        raise ValueError(
            f"Primary key '{primary_key}' not found in CSV for {entity_name}. "
            f"Available columns: {list(df.columns)}"
        )


def validate_generated_files(entity_name: str) -> None:
    model_file = MODELS_DIR / f"{entity_name}_model.py"
    router_file = ROUTERS_DIR / f"{entity_name}_router.py"

    if not model_file.exists():
        raise FileNotFoundError(f"Generated model not found: {model_file}")

    if not router_file.exists():
        raise FileNotFoundError(f"Generated router not found: {router_file}")

    router_content = router_file.read_text(encoding="utf-8")

    if 'load_csv_data("None")' in router_content:
        raise ValueError(
            f"Router for {entity_name} contains load_csv_data(\"None\"). "
            "Regenerate the router after fixing metadata_loader.py."
        )


def validate_imports(entity_name: str) -> None:
    model_module = f"app.models.generated.{entity_name}_model"
    router_module = f"app.routers.generated.{entity_name}_router"

    importlib.import_module(model_module)
    router = importlib.import_module(router_module)

    if not hasattr(router, "router"):
        raise AttributeError(
            f"Generated router module '{router_module}' does not expose a router object."
        )


def validate_main_import() -> None:
    main_module = importlib.import_module("app.main")

    if not hasattr(main_module, "app"):
        raise AttributeError("app/main.py does not expose an app object.")


def validate_entity(entity_name: str) -> dict:
    entity = validate_metadata(entity_name)

    csv_file = entity["csv_file"]
    primary_key = entity["primary_key"]

    validate_csv(entity_name, csv_file, primary_key)
    validate_generated_files(entity_name)
    validate_imports(entity_name)

    return {
        "entity": entity_name,
        "domain": entity.get("domain"),
        "csv_file": csv_file,
        "primary_key": primary_key,
        "status": "OK",
    }


def validate_generated_api(entities: list[str] | None = None) -> dict:
    if entities is None:
        entities = get_all_entities()

    print("Global HR Generated API Validation")
    print("=" * 42)

    has_errors = False
    passed = []
    failed = []

    try:
        validate_main_import()
        print("app/main.py          OK | FastAPI app importable")
    except Exception as error:
        has_errors = True
        failed.append({"entity": "app/main.py", "error": str(error)})
        print(f"app/main.py          FAIL | {error}")

    for entity_name in entities:
        try:
            result = validate_entity(entity_name)
            passed.append(result)

            print(
                f"{result['entity']:<20} OK | "
                f"domain={result['domain']} | "
                f"csv={result['csv_file']} | "
                f"pk={result['primary_key']}"
            )

        except Exception as error:
            has_errors = True
            failed.append({"entity": entity_name, "error": str(error)})
            print(f"{entity_name:<20} FAIL | {error}")

    print("=" * 42)

    if has_errors:
        print("Validation completed with errors.")
        raise RuntimeError("Generated API validation failed.")

    print("All generated API checks passed.")

    return {
        "checked": len(entities),
        "passed": len(passed),
        "failed": len(failed),
        "failed_items": failed,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate generated Global HR API data products."
    )

    parser.add_argument(
        "--entities",
        nargs="+",
        required=False,
        help="Entity names to validate. Example: applications workers candidates",
    )

    args = parser.parse_args()

    try:
        validate_generated_api(args.entities)
    except RuntimeError:
        raise SystemExit(1)


if __name__ == "__main__":
    main()