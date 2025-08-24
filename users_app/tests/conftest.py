import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app import models

# Usar una base de datos SQLite en memoria para las pruebas
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture para la sesión de la base de datos de prueba
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

# Fixture para el cliente de prueba de FastAPI
@pytest.fixture(scope="function")
def client(db_session):
    # Función para anular la dependencia get_db
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    # Aplicar la anulación de la dependencia
    app.dependency_overrides[get_db] = override_get_db
    
    yield TestClient(app)

    # Limpiar la anulación después de la prueba
    app.dependency_overrides.clear()
