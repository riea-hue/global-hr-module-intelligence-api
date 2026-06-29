# -----------------------------------------------------------------------------
# RIEA — Applied Intellectual and Ethical Responsibility
#
# AI-assisted with ChatGPT 5.5
# Human-reviewed, validated, and ethically owned by PAMB
#
# Technical Signature: Asanae ♠
# -----------------------------------------------------------------------------

from importlib import import_module
from pathlib import Path

from fastapi import FastAPI


BASE_DIR = Path(__file__).resolve().parent.parent
GENERATED_ROUTERS_DIR = BASE_DIR / "routers" / "generated"


def discover_generated_router_modules() -> list[str]:
    if not GENERATED_ROUTERS_DIR.exists():
        return []

    router_modules = []

    for file_path in GENERATED_ROUTERS_DIR.glob("*_router.py"):
        if file_path.name == "__init__.py":
            continue

        module_name = file_path.stem
        import_path = f"app.routers.generated.{module_name}"
        router_modules.append(import_path)

    return sorted(router_modules)


def register_generated_routers(app: FastAPI) -> None:
    router_modules = discover_generated_router_modules()

    for module_path in router_modules:
        module = import_module(module_path)

        if not hasattr(module, "router"):
            raise AttributeError(
                f"Generated router module '{module_path}' does not expose a 'router' object."
            )

        app.include_router(module.router)
