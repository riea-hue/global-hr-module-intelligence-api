# -----------------------------------------------------------------------------
# RIEA — Applied Intellectual and Ethical Responsibility
#
# AI-assisted with ChatGPT 5.5
# Human-reviewed, validated, and ethically owned by PAMB
#
# Technical Signature: Asanae ♠
# -----------------------------------------------------------------------------

from fastapi import FastAPI

from app.routers.metadata_router import router as metadata_router
from app.services.openapi_enrichment_service import enrich_openapi
from engine.generators.metadata_loader import MetadataLoader
from engine.registry.router_registry import register_generated_routers

app = FastAPI(
    title="Global HR Module Intelligence API",
    version="1.0.0",
    description=(
        "Open-source HR Technology sandbox with metadata-driven REST APIs, "
        "synthetic HR data, OData-style querying, RBAC, and generated documentation."
    ),
)


metadata_loader = MetadataLoader()


@app.get("/")
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "project": "Global HR Module Intelligence API",
        "version": "1.0.0",
        "framework": "Metadata-driven HR Technology Sandbox",
    }


app.include_router(metadata_router)

register_generated_routers(app)

enrich_openapi(app, metadata_loader)