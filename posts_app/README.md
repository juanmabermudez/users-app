# Microservicio de Publicaciones (posts_app)

## Estado Actual

🚧 **En desarrollo** - Este microservicio está planificado para entregas futuras.

## Descripción

El microservicio de Publicaciones será responsable de gestionar las publicaciones de ofertas de envío creadas por los usuarios. Este servicio manejará la lógica de negocio relacionada con:

- Creación y gestión de publicaciones
- Asociación de publicaciones con trayectos específicos
- Gestión del ciclo de vida de las publicaciones (creación, expiración)

## Funcionalidades Planificadas

- **Gestión de Publicaciones**: CRUD completo para publicaciones
- **Integración con Usuarios**: Asociación de publicaciones con usuarios
- **Integración con Trayectos**: Vinculación con rutas específicas
- **Gestión de Fechas de Expiración**: Control automático de vencimiento

## Tecnologías

- **Backend**: FastAPI (Python)
- **Base de Datos**: PostgreSQL
- **ORM**: SQLAlchemy

## Endpoints Planificados

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/posts` | Crear nueva publicación |
| GET | `/posts` | Listar publicaciones |
| GET | `/posts/{id}` | Obtener publicación específica |
| PATCH | `/posts/{id}` | Actualizar publicación |
| DELETE | `/posts/{id}` | Eliminar publicación |
| GET | `/posts/ping` | Health check |

## Estado de Implementación

- [ ] Estructura del proyecto
- [ ] Modelos de datos
- [ ] API REST
- [ ] Pruebas unitarias
- [ ] Dockerización
- [ ] Manifiestos de Kubernetes
- [ ] Documentación completa

---

*Nota: Este microservicio será implementado en entregas posteriores según el cronograma del proyecto.*