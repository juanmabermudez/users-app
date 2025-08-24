# Microservicio de Ofertas (offers_app)

## Estado Actual

🚧 **En desarrollo** - Este microservicio está planificado para entregas futuras.

## Descripción

El microservicio de Ofertas será responsable de gestionar todas las ofertas realizadas por usuarios sobre publicaciones existentes. Este servicio manejará:

- Creación y gestión de ofertas sobre publicaciones
- Validación de ofertas según criterios de negocio
- Gestión de estados de ofertas (pendiente, aceptada, rechazada)
- Cálculo de métricas y puntuaciones

## Funcionalidades Planificadas

- **Gestión de Ofertas**: CRUD completo para ofertas
- **Validación de Negocio**: Reglas de validación para ofertas
- **Gestión de Estados**: Control del flujo de estados de ofertas
- **Integración con Publicaciones**: Asociación con publicaciones específicas
- **Sistema de Puntuación**: Cálculo de utilidad y métricas

## Tecnologías

- **Backend**: FastAPI (Python)
- **Base de Datos**: PostgreSQL
- **ORM**: SQLAlchemy

## Endpoints Planificados

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/offers` | Crear nueva oferta |
| GET | `/offers` | Listar ofertas |
| GET | `/offers/{id}` | Obtener oferta específica |
| PATCH | `/offers/{id}` | Actualizar oferta |
| DELETE | `/offers/{id}` | Eliminar oferta |
| GET | `/offers/ping` | Health check |

## Modelo de Datos Planificado

### Offer (Oferta)
- `id`: Identificador único
- `postId`: Referencia a la publicación
- `userId`: Referencia al usuario que hace la oferta
- `description`: Descripción del artículo a enviar
- `size`: Tamaño del artículo (LARGE, MEDIUM, SMALL)
- `fragile`: Indicador si el artículo es frágil
- `offer`: Monto ofrecido
- `createdAt`: Fecha de creación

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