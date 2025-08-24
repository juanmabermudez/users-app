# Users - Proyecto ejemplo

Este proyecto es un ejemplo de una aplicación FastAPI que implementa una arquitectura hexagonal (puertos y adaptadores) para gestionar la entidad **User**. La aplicación puede ejecutarse en Docker y en minikube.

Con este proyecto aprenderás:

- Cómo construir una aplicación siguiendo principios SOLID con Python, FastAPI, Poetry y Pytest.
- Cómo ejecutar la aplicación con Docker siguiendo buenas prácticas.
- Cómo automatizar pruebas de API con Postman.
- Cómo ejecutar la aplicación en minikube y prepararla para ambientes productivos en k8s.
- Cómo configurar pipelines en GitHub para pruebas unitarias, linters y pruebas de API.

## Tabla de contenido

- [Users - Proyecto ejemplo](#users---proyecto-ejemplo)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Requisitos](#requisitos)
  - [Estructura del Proyecto](#estructura-del-proyecto)
    - [Carpeta src](#carpeta-src)
      - [Domain](#domain)
      - [Adapters](#adapters)
      - [Entrypoints](#entrypoints)
      - [Configuración y ensamble](#configuración-y-ensamble)
      - [Errores](#errores)
    - [Configuración](#configuración)
  - [Ejecución de la aplicación](#ejecución-de-la-aplicación)
  - [Ejecutar en Docker](#ejecutar-en-docker)
  - [Ejecutar en minikube](#ejecutar-en-minikube)
  - [API Endpoints](#api-endpoints)
  - [User Model](#user-model)
  - [Pruebas](#pruebas)
    - [Unitarias](#unitarias)
    - [Integración](#integración)
  - [Pipelines](#pipelines)
  - [Cómo contribuir](#cómo-contribuir)
  - [Licencia](#licencia)
  - [Autor](#autor)

## Requisitos

- Python 3.11
- Poetry >= 2.1.1
- Docker
- Postman

## Estructura del Proyecto

```
.
├── src/
│   ├── domain/             # Capa de dominio
│   │   ├── models/         # Modelos de dominio
│   │   ├── ports/          # Puertos (interfaces)
│   │   └── use_cases/      # Casos de uso
│   ├── adapters/           # Adaptadores (ej: memoria, base de datos)
│   └── entrypoints/        # Puntos de entrada (API REST)
├── tests/                  # Pruebas unitarias e integración
├── Dockerfile              # Configuración de Docker
├── pyproject.toml          # Configuración de Poetry
└── README.md               # Este archivo
```

### Carpeta src

Contiene el código principal de la aplicación.

#### Domain

- `/domain/models`: Clases que representan las entidades del dominio (**User**).
- `/domain/ports`: Interfaces para interacción con componentes externos (ej: repositorios).
- `/domain/use_cases`: Casos de uso (crear, consultar, modificar, borrar usuarios).

Ejemplo de modelo:
```python
# domain/models/user.py
class User(BaseModel):
    id: int | None = None
    username: str = Field(min_length=1)
    email: EmailStr
    fullName: str
    dni: str
    phoneNumber: str
    status: str
    password: str
```

Ejemplo de puerto:
```python
# domain/ports/user_repository_port.py
class UserRepositoryPort(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass
    ...
```

Ejemplo de caso de uso:
```python
# domain/use_cases/create_user_use_case.py
class CreateUserUseCase(BaseUseCase):
    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    def execute(self, user: User) -> User:
        return self.user_repository.create(user)
```

#### Adapters

Implementaciones de los puertos, por ejemplo almacenamiento en memoria:

```python
# adapters/memory/user_repository_adapter.py
class InMemoryUserRepositoryAdapter(UserRepositoryPort):
    memory_store: Dict[int, User] = {}
    _id_counter: int = 1

    def sequence(self) -> int:
        current_id = self._id_counter
        self._id_counter += 1
        return current_id

    def create(self, user: User) -> User:
        user.id = self.sequence()
        self.memory_store[user.id] = user
        return user
    ...
```

#### Entrypoints

Routers de FastAPI que exponen los endpoints:

```python
router = APIRouter(prefix="/users")

@router.get("/ping", response_class=PlainTextResponse)
def health_check():
    return "pong"
```

Agrega el router en `main.py`:

```python
app = FastAPI(title=Settings.app_name)
app.include_router(user_router)
```

#### Configuración y ensamble

- `config.py`: Variables de ambiente y constantes.
- `assembly.py`: Inyección de dependencias, instanciación de adaptadores y casos de uso.

Ejemplo:
```python
# assembly.py
repository = InMemoryUserRepositoryAdapter()

def build_create_user_use_case() -> BaseUseCase:
    return CreateUserUseCase(repository)
...
```

#### Errores

Define excepciones personalizadas en `errors.py`:

```python
class UserNotFoundError(Exception):
    pass
```

Y su handler en FastAPI:

```python
@app.exception_handler(UserNotFoundError)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(status_code=404, content={"detail": str(exc)})
```
### Configuración

Usa Poetry para gestionar dependencias y configuración en `pyproject.toml`.

- Instala dependencias de producción:
  ```
  poetry add <libreria>
  ```
- Instala dependencias de desarrollo:
  ```
  poetry add <libreria> --group dev
  ```
- Ejecuta:
  ```
  poetry lock
  ```

## Ejecución de la aplicación

1. **Instala dependencias:**
   ```
   poetry install
   ```

2. **Ejecuta el servidor:**
   ```
   PYTHONPATH=$(pwd)/src poetry run uvicorn entrypoints.api.main:app --host 0.0.0.0 --port 9000
   ```

El API estará disponible en `http://localhost:9000`.

Cargue el archivo `pets_app/tests/api/pets.postman_collection.json` en su postman y reemplace la variable `baseUrl` por la url.

Ejecute las pruebas y verifique que se completa correctamente.

## Ejecutar en Docker

```bash
APP_VERSION=... # usa la versión de pyproject.toml
APP_NAME=...    # usa el nombre definido en pyproject.toml
docker build --rm --platform linux/amd64 -t ${APP_NAME}:${APP_VERSION} -f Dockerfile --target runner --label version=${APP_VERSION} .
docker run --platform linux/amd64 -p 9000:9000 ${APP_NAME}:${APP_VERSION}
```

## Ejecutar en minikube

```bash
minikube start --cpus=2 --memory=3g --cni calico
minikube image load ${APP_NAME}:${APP_VERSION}
kubectl apply -f k8s
minikube service users-service
```

## API Endpoints

- `POST /users/` - Crea un usuario
- `GET /users/{user_id}` - Consulta un usuario específico
- `GET /users/` - Lista todos los usuarios
- `PUT /users/{user_id}` - Modifica un usuario
- `PATCH /users/{user_id}` - Actualiza parcialmente un usuario
- `DELETE /users/{user_id}` - Elimina un usuario
- `GET /users/count` - Devuelve el número de usuarios
- `POST /users/auth` - Autentica usuario y retorna token
- `GET /users/me` - Consulta el usuario autenticado
- `POST /users/reset` - Resetea el almacenamiento en memoria

Consulta la documentación interactiva en:
- Swagger UI: `http://localhost:9000/docs`

## User Model

Un usuario tiene los siguientes campos:
- `id`: Integer (auto-generado)
- `username`: String
- `email`: Email
- `fullName`: String
- `dni`: String
- `phoneNumber`: String
- `status`: String
- `password`: String

## Pruebas

El proyecto incluye pruebas unitarias y de integración.

### Unitarias

Ubica las pruebas siguiendo la estructura de la carpeta src.  
Ejemplo:  
Para `domain/models/user.py`, crea `tests/unit/domain/models/test_user.py`.

Usa fixtures en `conftest.py`:

```python
@pytest.fixture
def valid_user_data():
    return {
        "username": "testuser",
        "email": "testuser@example.com",
        "fullName": "Test User",
        "dni": "12345678",
        "phoneNumber": "5551234",
        "status": "POR_VERIFICAR",
        "password": "password123"
    }
```

Ejecuta las pruebas unitarias y mide cobertura:
```bash
poetry run pytest --cov=src -v -s --cov-fail-under=70 --cov-report term-missing
```

### Integración

Las pruebas de integración se realizan con Postman y Newman.  
Carga la colección en `tests/api/users.postman_collection.json` en Postman y ejecuta las pruebas.

## Pipelines

Ejemplos de configuración en `.github/workflows/`.  
Incluye pruebas unitarias, linters y pruebas de API.

## Cómo contribuir

Sigue las reglas definidas en la carpeta `.cursor` para agregar nuevas funcionalidades.

## Licencia

MIT - ver [LICENSE](LICENSE).

## Autor

- César