# Usar una imagen base de Python ligera y segura
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar poetry
RUN pip install poetry

# Copiar los archivos de dependencias primero para aprovechar la caché de Docker
# El asterisco en poetry.lock* es para que coincida si el archivo existe
COPY pyproject.toml poetry.lock* ./

# Instalar las dependencias del proyecto sin instalar el paquete raíz
# --no-root es una buena práctica para imágenes de producción/despliegue
RUN poetry install --no-root

# Copiar el resto del código fuente de la aplicación
COPY ./app /app/app

# Exponer el puerto en el que la aplicación se ejecutará
EXPOSE 8000

# Comando para ejecutar la aplicación al iniciar el contenedor
# Usar "poetry run" para ejecutar dentro del entorno virtual de poetry
# --host 0.0.0.0 es crucial para que la aplicación sea accesible desde fuera del contenedor
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
