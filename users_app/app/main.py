from fastapi import FastAPI
from . import models
from .database import engine
from .routers import users

# Crea las tablas en la base de datos al iniciar la aplicación
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Users Service API",
    description="API for managing users in the cloud application project.",
    version="1.0.0"
)

# Incluir el router de usuarios
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Users Service"}
