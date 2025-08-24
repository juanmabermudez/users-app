Este archivo README.md fue eliminado porque no corresponde a la implementación de la API de usuarios.
.
├── github/
│   └── workflows/          # Pipelines del repositorio
├── k8s/                    # Archivos para despliegue en k8s
├── docs/                   # Archivos de documentación técnica
├── <aplicación>            # Archivos de aplicación. Una carpeta por cada una.
├── vale.ini                # Configuración para Vale. NO MODIFICAR
├── config.yaml             # Configuración del repositorio. Modifíquelo como primera tarea
├── Makefile                # Scripts para evaluación. NO MODIFICAR las reglas actuales
└── README.md               # Este archivo
```

1. **github/workflows**: los archivos en esta carpeta no se pueden modificar a excepción del archivo `ci_evaluador_unit.yml` el cuál debe ser utilizado para agregar un job por cada aplicación.
   * `ci_evaluador_entrega1_k8s.yml` verifica configuración de k8s y ejecuta pruebas sobre cada aplicación. Su modificación anula su entrega.
   * `ci_evaluador_entrega1_docs.yml` verifica que los diagramas de la documentación contengan los componentes esperados, hace una revisión gramática sobre el contenido del markdown. Su modificación anula su entrega.
   * `ci_evaluador_unit.yml` ejecuta pruebas unitarias. Modifique este archivo agregando un job por aplicación.
2. **k8s**: Archivos de configuración y despliegue de sus aplicaciones. Puede crear un archivo por aplicación o todos en un mismo archivo. La decisión de la estructura es suya.
3. **docs**: Archivos de la documentación técnica. Debe existir un archivo `README.md` para que se genere la página de la documentación en `github pages` y la carpeta `diagrams` con los archivos `puml` en esta. La estructura de la documentación es decisión del equipo.
4. **<aplicación>**: Una carpeta por cada aplicación. A continuación se habla en más detalle de su estructura.
5. **makefile**: El archivo `makefile` es utilizado por los pipelines evaluadores, **NO** modifique los scripts que encontrará allí, pero si puede agregar nuevos si así lo requiere.

## Archivo de configuración

El archivo `config.yaml` es el archivo más importante en el repositorio. Este archivo contiene la configuración que se usa en los pipelines para evaluar su entrega y se define la calificación de cada miembro del equipo. Si este archivo no está correctamente configurado, su entrega no puede ser calificada y será de cero.

## Estructura de cada aplicación

Cada aplicación debe seguir las siguientes reglas:

1. Cada aplicación debe estar en una carpeta independente y construida en el lenguaje de su preferencia. En este repositorio encontrará cómo ejemplo la aplicación `pets_app` construida en `Python`, `Poetry`, `FastAPI` y `Pytest`.
2. Dentro de cada carpeta de aplicación debe estar el archivo `Dockerfile` que permite la ejecución de la aplicación. Este archivo debe estar en la raiz de la carpeta y no en otras ubicaciones.
3. El nombre de la carpeta es decisión libre del equipo pero debe estar registrado en el archivo `config.yaml` o de lo contrario no podrá ser evaluado.
4. El nombre y tag de cada imagen deben ser agregadas en el archivo `config.yaml` y deben corresponder a los mismos que se usan en la configuración de despliegue de k8s. Si la configuración de este archivo no es correcta, su evaluación fallará y la nota será de cero.

Lo invitamos a revisar el archivo `README.md` de la carpeta [pets](./pets_app/) donde encontrará la documentación para utilizar ese proyecto en `Python` como su ejemplo.
=======
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
>>>>>>> main
