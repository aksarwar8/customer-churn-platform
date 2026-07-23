from fastapi import Request
from fastapi.responses import JSONResponse

from src.logger import logger


async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled Exception: {exc}")

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Something went wrong while processing the request."
        }
    )