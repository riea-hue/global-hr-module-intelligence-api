from pathlib import Path

from engine.generators.metadata_loader import MetadataLoader
from engine.generators.model_generator import generate_model
from engine.generators.router_generator import generate_router


BASE_DIR = Path(__file__).resolve().parent.parent


def get_entities() -> list[str]:
    loader = MetadataLoader()
    resources = loader.api_catalog.get("resources", [])

    entities = [
        resource.get("source_table")
        for resource in resources
        if resource.get("source_table")
    ]

    return sorted(set(entities))


def generate_all_data_products() -> dict:
    entities = get_entities()

    generated = []
    failed = []

    print("Global HR Data Product Bulk Generator")
    print("=" * 45)

    for entity in entities:
        try:
            print(f"Generating: {entity}")

            generate_model(entity)
            generate_router(entity)

            generated.append(entity)
            print(f"Generated: {entity}")

        except Exception as error:
            failed.append(
                {
                    "entity": entity,
                    "error": str(error),
                }
            )

            print(f"Failed: {entity} | {error}")

    print("=" * 45)
    print(f"Detected entities: {len(entities)}")
    print(f"Generated count: {len(generated)}")
    print(f"Failed count: {len(failed)}")

    if failed:
        print("Failed entities:")
        for item in failed:
            print(f"- {item['entity']}: {item['error']}")

        raise RuntimeError("One or more data products failed to generate.")

    print("All data products generated successfully.")

    return {
        "detected": len(entities),
        "generated": len(generated),
        "failed": len(failed),
        "entities": generated,
    }


if __name__ == "__main__":
    generate_all_data_products()