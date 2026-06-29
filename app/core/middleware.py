import time

from fastapi import Request

from app.core.logger import logger


async def request_logger(request: Request, call_next):

    start = time.perf_counter()

    response = await call_next(request)

    duration = round((time.perf_counter() - start) * 1000, 2)

    logger.info(
        "%s %s -> %s (%sms)",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )

    return response
