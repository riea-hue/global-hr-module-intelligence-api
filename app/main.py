# -----------------------------------------------------------------------------
# RIEA — Applied Intellectual and Ethical Responsibility
#
# AI-assisted with ChatGPT 5.5
# Human-reviewed, validated, and ethically owned by PAMB
#
# Technical Signature: Asanae ♠
# -----------------------------------------------------------------------------

from fastapi import FastAPI

from app.api.routers.system import router as system_router
from app.core.exceptions import register_exception_handlers
from app.core.middleware import request_logger
from app.core.settings import settings
from app.generators.router_generator import dynamic_router
from app.routers.metadata import router as metadata_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Metadata-driven Enterprise HR API powered by Global HR JSON contracts.",
)

app.middleware("http")(request_logger)

register_exception_handlers(app)

app.include_router(system_router)
app.include_router(metadata_router)
app.include_router(dynamic_router)


@app.get("/")
def root():
    return {
        "name": settings.APP_NAME,
        "status": "running",
        "docs": "/docs",
    }
