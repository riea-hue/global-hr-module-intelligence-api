from pathlib import Path

from documentation.context_builder import DocumentationContextBuilder
from documentation.engine import DocumentationEngine


BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATE_DIR = BASE_DIR / "documentation" / "templates"
OUTPUT_FILE = BASE_DIR / "README.md"

TEMPLATE_NAME = "README.md.j2"


def generate_readme() -> None:
    print("Building documentation context...")

    context = DocumentationContextBuilder().build()

    print("Rendering README template...")

    engine = DocumentationEngine(TEMPLATE_DIR)

    content = engine.render(
        TEMPLATE_NAME,
        context,
    )

    engine.write(
        OUTPUT_FILE,
        content,
    )

    print(f"README generated successfully:\n{OUTPUT_FILE}")


if __name__ == "__main__":
    generate_readme()