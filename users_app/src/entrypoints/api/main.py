from fastapi import FastAPI

from config import Settings
from entrypoints.api.routers.user_router import router as user_router

app = FastAPI(title=Settings.app_name)
app.include_router(user_router)
