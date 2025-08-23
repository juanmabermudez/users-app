from fastapi import FastAPI, Request

from config import Settings
from fastapi.responses import JSONResponse
from entrypoints.api.routers.user_router import router as user_router
from fastapi.exception_handlers import RequestValidationError
from fastapi.exceptions import RequestValidationError

app = FastAPI(title=Settings.app_name)
app.include_router(user_router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"error": "Missing or invalid fields", "details": exc.errors()},
    )
