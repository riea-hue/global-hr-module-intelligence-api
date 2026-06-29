from fastapi import APIRouter

from app.core.settings import settings

router = APIRouter(tags=["System"])


@router.get("/health")
def health():

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "provider": settings.PROVIDER,
    }


@router.get("/version")
def version():

    return {"version": settings.VERSION}
