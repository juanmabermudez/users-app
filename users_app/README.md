# users_app

Microservicio para la gestión de usuarios.

## Estructura

- `app/` - Código fuente principal
- `tests/` - Pruebas unitarias
- `Dockerfile` - Imagen de despliegue

## Variables de entorno

- `DATABASE_URL` - URL de conexión a PostgreSQL

## Ejecución local

```sh
poetry install
poetry run uvicorn app.main:app --reload
```

## Pruebas

```sh
poetry run pytest --cov=app --cov-report=term-missing --cov-fail-under=70
```
# Microservicio de Usuarios (users_app)

## Descripción

El microservicio de Usuarios es el responsable de gestionar toda la información y la lógica de negocio relacionada con los usuarios del sistema. Proporciona una API REST para la creación, actualización, autenticación y consulta de perfiles de usuario.

## API Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/users` | Crea un nuevo usuario. |
| PATCH | `/users/{id}` | Actualiza la información de un usuario existente. |
| POST | `/users/auth` | Autentica a un usuario y genera un token de sesión. |
| GET | `/users/me` | Consulta la información del usuario autenticado. |
| GET | `/users/count` | Devuelve el número total de usuarios registrados. |
| GET | `/users/ping` | Verifica la salud y disponibilidad del servicio. |
| POST | `/users/reset` | Elimina todos los usuarios de la base de datos. |

## Variables de Ambiente

Para su ejecución, la aplicación requiere las siguientes variables de ambiente:

- `DATABASE_URL`: La URL de conexión a la base de datos PostgreSQL. Formato: `postgresql://user:password@host:port/dbname`

## Desarrollo Local

**Navegar al directorio:**
```bash
cd users_app
```

**Instalar dependencias:**
Se recomienda usar Poetry para la gestión de dependencias.
```bash
poetry install
```

**Ejecutar la aplicación:**
El servidor se iniciará en http://127.0.0.1:8000.
```bash
poetry run uvicorn app.main:app --reload
```

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias y generar un informe de cobertura de código, utilice el siguiente comando desde el directorio `users_app`:

```bash
poetry run pytest --cov=app --cov-report=term-missing --cov-fail-under=70
```
