from time import perf_counter

from engine.generators.bulk_generate import generate_all_data_products
from documentation.generate_all import generate_all_documentation
from scripts.validate_generated_api import validate_generated_api


def banner() -> None:
    print()
    print("=" * 70)
    print("Global HR Intelligence API")
    print("Enterprise Build Pipeline")
    print("=" * 70)
    print()


def step(title: str, fn):
    print(f"[BUILD] {title}...")

    start = perf_counter()

    result = fn()

    elapsed = perf_counter() - start

    print(f"[ OK ] {title} ({elapsed:.2f}s)")
    print()

    return result


def main() -> None:
    banner()

    generation_result = step(
        "Generating Data Products, Models and Routers",
        generate_all_data_products,
    )

    step(
        "Generating Documentation",
        generate_all_documentation,
    )

    step(
        "Validating Generated API",
        validate_generated_api,
    )

    print("=" * 70)
    print("BUILD COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print(f"Entities detected : {generation_result.get('detected')}")
    print(f"Entities generated: {generation_result.get('generated')}")
    print(f"Entities failed   : {generation_result.get('failed')}")
    print("=" * 70)


if __name__ == "__main__":
    main()