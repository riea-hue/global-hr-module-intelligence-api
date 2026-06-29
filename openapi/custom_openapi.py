from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        summary=getattr(app, "summary", None),
        description=app.description,
        routes=app.routes,
        contact=app.contact,
        license_info=app.license_info,
    )

    openapi_schema["x-framework"] = "Global HR Intelligence API"
    openapi_schema["x-author"] = "PAMB"
    openapi_schema["x-signature"] = "Asanae ♠"
    openapi_schema["x-identity"] = {
        "brand": "RIEA",
        "principle": "Applied Intellectual and Ethical Responsibility",
        "human_owner": "PAMB",
        "ai_assisted": True,
    }
    openapi_schema["x-version-history"] = [
        {
            "version": "1.0.0",
            "status": "rebuild",
            "description": "Clean rebuild after local folder corruption.",
        }
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema
