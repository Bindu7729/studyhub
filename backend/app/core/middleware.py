"""HTTP Request logging and timing middleware for StudyHub API."""
import time
import logging
from typing import Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("studyhub.api")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.perf_counter()
        method = request.method
        url_path = request.url.path

        try:
            response = await call_next(request)
            process_time_ms = (time.perf_counter() - start_time) * 1000.0
            response.headers["X-Process-Time-Ms"] = f"{process_time_ms:.2f}"
            
            # Log successful or non-server-error requests
            if response.status_code < 400:
                logger.info(f"{method} {url_path} -> {response.status_code} ({process_time_ms:.1f}ms)")
            else:
                logger.warning(f"{method} {url_path} -> {response.status_code} ({process_time_ms:.1f}ms)")
            return response
        except Exception as exc:
            process_time_ms = (time.perf_counter() - start_time) * 1000.0
            logger.error(f"{method} {url_path} failed after {process_time_ms:.1f}ms: {exc}", exc_info=True)
            raise exc
