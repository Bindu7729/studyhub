"""Centralized exception handling and error response models for StudyHub API."""
from typing import Any, Optional, Dict
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


class StudyHubException(Exception):
    """Base class for domain-specific application exceptions."""
    def __init__(
        self,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        error_code: str = "BAD_REQUEST",
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.details = details or {}


class ResourceNotFoundError(StudyHubException):
    def __init__(self, resource: str, identifier: Any):
        super().__init__(
            message=f"{resource} with identifier '{identifier}' was not found.",
            status_code=status.HTTP_404_NOT_FOUND,
            error_code="NOT_FOUND",
            details={"resource": resource, "identifier": str(identifier)},
        )


class CodeExecutionTimeoutError(StudyHubException):
    def __init__(self, timeout_seconds: int):
        super().__init__(
            message=f"Code execution exceeded the allowable limit of {timeout_seconds} seconds.",
            status_code=status.HTTP_408_REQUEST_TIMEOUT,
            error_code="EXECUTION_TIMEOUT",
            details={"timeout_seconds": timeout_seconds},
        )


async def studyhub_exception_handler(request: Request, exc: StudyHubException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": exc.error_code,
                "message": exc.message,
                "details": exc.details,
            },
        },
    )


async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {
                "code": f"HTTP_{exc.status_code}",
                "message": str(exc.detail),
                "details": {},
            },
        },
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    errors = []
    for err in exc.errors():
        loc = " -> ".join([str(x) for x in err.get("loc", [])])
        errors.append({
            "field": loc,
            "message": err.get("msg", ""),
            "type": err.get("type", "")
        })
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Input validation failed.",
                "details": {"validation_errors": errors},
            },
        },
    )
