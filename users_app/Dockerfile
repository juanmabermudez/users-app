# syntax=docker/dockerfile:1

############################
# Stage 1: builder (Poetry)
############################
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.3 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1

WORKDIR /app

# Paquetes base (solo lo mínimo para compilar ruedas cuando haga falta)
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential curl \
 && rm -rf /var/lib/apt/lists/*

# Instala Poetry
RUN pip install --no-cache-dir "poetry==${POETRY_VERSION}"

# Copia solo archivos de dependencias para maximizar caché
COPY pyproject.toml poetry.lock* ./

# Instala dependencias de runtime dentro de .venv (sin código aún)
# --no-root porque este proyecto es "package-mode = false"
RUN poetry install --only main --no-interaction --no-ansi

# Copia el código (para correr tests/build opcional si hiciera falta)
COPY src ./src

############################
# Stage 2: runner (rootless)
############################
FROM python:3.11-slim AS runner

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Usuario no root
RUN useradd -u 10001 -m appuser

# Paquetes mínimos para healthcheck
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

# Copia el venv creado por Poetry en /app/.venv desde builder
COPY --from=builder /app/.venv /opt/venv

# Añade el venv al PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copia el código fuente
COPY src ./src

# Puerto de la aplicación (README indica 9000)
EXPOSE 9000

# Permite ajustar el módulo ASGI sin rehacer la imagen si cambias la app
# En este repo la app está en src/entrypoints/api/main.py con objeto "app"
ARG APP_MODULE="entrypoints.api.main:app"
ENV APP_MODULE=${APP_MODULE}

# Healthcheck sencillo contra el OpenAPI (no hay /health en el código)
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD curl -fsS "http://127.0.0.1:9000/openapi.json" >/dev/null || exit 1

# Cambia a usuario no root
USER appuser

# Ejecuta Uvicorn (sin --reload en producción)
CMD ["sh", "-c", "uvicorn ${APP_MODULE} --host 0.0.0.0 --port 9000"]
