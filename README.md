# Proyecto Microservicios DANN

## Estructura de carpetas

- `users_app/` - Microservicio de usuarios
- `posts_app/` - Microservicio de publicaciones
- `routes_app/` - Microservicio de rutas
- `offers_app/` - Microservicio de ofertas
- `k8s/` - Manifiestos de Kubernetes
- `docs/` - Documentación técnica y diagramas

## Despliegue local

1. Instala Docker, Minikube, Poetry y Python 3.12+.
2. Inicia Minikube:
   ```sh
   minikube start --driver=docker
   ```
3. Construye la imagen y despliega:
   ```sh
   docker build -t users-app-image:v1.0.0 users_app/
   kubectl apply -f k8s/
   ```
4. Accede a los servicios:
   ```sh
   minikube service users-app-service
   ```

## CI/CD

Los pipelines se ejecutan automáticamente en cada push a main o develop.
# Proyecto de Aplicaciones Nativas en la Nube

Este repositorio contiene la implementación de un sistema de microservicios para el curso de Aplicaciones Nativas en la Nube.

## Estructura del Proyecto

```
/
├── .github/
│   └── workflows/      # Pipelines de CI/CD
├── docs/               # Documentación técnica del proyecto
│   ├── diagrams/       # Archivos fuente de PlantUML
│   └── ...            # Otros archivos Markdown para las vistas
├── k8s/                # Manifiestos de despliegue de Kubernetes
├── users_app/          # Microservicio de Usuarios
├── posts_app/          # Microservicio de Publicaciones
├── offers_app/         # Microservicio de Ofertas
├── routes_app/         # Microservicio de Trayectos
└── config.yaml         # Archivo de configuración central del proyecto
```

## Microservicios Implementados

### 1. Microservicio de Usuarios (users_app)

El microservicio de usuarios es responsable de gestionar toda la información y lógica de negocio relacionada con los usuarios del sistema.

**Características:**
- API REST completa para gestión de usuarios
- Autenticación con tokens JWT
- Hashing seguro de contraseñas con bcrypt
- Base de datos PostgreSQL
- Pruebas unitarias con cobertura >70%

**Endpoints disponibles:**
- `POST /users` - Crear usuario
- `PATCH /users/{id}` - Actualizar usuario
- `POST /users/auth` - Autenticación
- `GET /users/me` - Obtener información del usuario autenticado
- `GET /users/count` - Contar usuarios
- `GET /users/ping` - Health check
- `POST /users/reset` - Resetear base de datos

## Tecnologías Utilizadas

- **Backend:** FastAPI (Python)
- **Base de Datos:** PostgreSQL
- **ORM:** SQLAlchemy
- **Autenticación:** JWT Tokens
- **Hashing:** bcrypt
- **Containerización:** Docker
- **Orquestación:** Kubernetes
- **CI/CD:** GitHub Actions
- **Gestión de Dependencias:** Poetry
- **Pruebas:** pytest, coverage

## Configuración del Proyecto

### Requisitos Previos

- Python 3.11+
- Docker
- Kubernetes (Minikube recomendado)
- Poetry

### Instalación y Configuración

1. **Clonar el repositorio:**
   ```bash
   git clone <repository-url>
   cd users-app
   ```

2. **Configurar el archivo config.yaml:**
   Editar el archivo `config.yaml` en la raíz del proyecto con la información de tu equipo.

3. **Desarrollo Local del Microservicio de Usuarios:**
   ```bash
   cd users_app
   poetry install
   poetry run uvicorn app.main:app --reload
   ```

4. **Ejecutar Pruebas:**
   ```bash
   cd users_app
   poetry run pytest --cov=app --cov-report=term-missing --cov-fail-under=70
   ```

## Despliegue en Kubernetes

### Con Minikube

1. **Iniciar Minikube:**
   ```bash
   minikube start
   ```

2. **Construir la imagen Docker:**
   ```bash
   eval $(minikube docker-env)
   docker build -t users-app-image:v1.0.0 users_app/
   ```

3. **Desplegar en Kubernetes:**
   ```bash
   kubectl apply -f k8s/
   ```

4. **Verificar el despliegue:**
   ```bash
   kubectl get pods
   kubectl get services
   ```

5. **Acceder al servicio:**
   ```bash
   minikube service users-app-service
   ```

## Pipelines de CI/CD

El proyecto incluye tres pipelines de CI/CD:

1. **ci_evaluador_unit.yml** - Ejecuta pruebas unitarias y valida cobertura de código
2. **ci_evaluador_docs.yml** - Valida documentación y diagramas PlantUML
3. **ci_evaluador_entrega1_k8s.yml** - Valida manifiestos de Kubernetes

## Documentación

- **Diagramas:** Los diagramas de arquitectura se encuentran en `docs/diagrams/`
- **API Documentation:** Disponible en `/docs` cuando el servicio está ejecutándose
- **READMEs específicos:** Cada microservicio tiene su propio README.md

## Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto es parte del curso de Aplicaciones Nativas en la Nube.
