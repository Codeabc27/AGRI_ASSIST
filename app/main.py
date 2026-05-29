import logging
import traceback

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import HTTPException

from app.api.routes.advisor import router as advisor_router
from app.api.routes.crop import router as crop_router
from app.api.routes.disease import router as disease_router
from app.api.routes.rag import router as rag_router
from app.api.routes.weather import router as weather_router

app = FastAPI(title="AgriAssist API")


# Basic logger
logger = logging.getLogger("agri_assist")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(f"HTTP error for {request.url.path}: {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Validation error for {request.url.path}: {exc}")
    return JSONResponse(
        status_code=422, content={"error": "Invalid request", "details": exc.errors()}
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    # Log full traceback for debugging
    tb = traceback.format_exc()
    logger.error(f"Unhandled exception for {request.url.path}: {tb}")
    return JSONResponse(status_code=500, content={"error": "Internal Server Error"})


app.include_router(rag_router)
app.include_router(crop_router)
app.include_router(disease_router)
app.include_router(weather_router)
app.include_router(advisor_router)


@app.get("/")
def home():
    return {"message": "AgriAssist Running"}
