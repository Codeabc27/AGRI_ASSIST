from fastapi import HTTPException


class AppError(HTTPException):
    """Custom application exception for predictable errors.

    Use `raise AppError(status_code=400, detail="...")` in services.
    """

    def __init__(self, status_code: int = 400, detail: str = "Application error"):
        super().__init__(status_code=status_code, detail=detail)


def wrap_exception(exc: Exception, msg: str = "Internal error") -> HTTPException:
    """Convert unexpected exceptions into HTTPException for consistent responses."""
    return HTTPException(status_code=500, detail=msg)
