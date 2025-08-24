# Microservicio de Trayectos (routes_app)

## Estado Actual

🚧 **En desarrollo** - Este microservicio está planificado para entregas futuras.

## Descripción

El microservicio de Trayectos será responsable de gestionar toda la información relacionada con rutas de vuelo y trayectos disponibles en el sistema. Este servicio manejará:

- Gestión de rutas de vuelo
- Información de aeropuertos y países
- Costos asociados al equipaje
- Fechas y horarios de vuelos planificados

## Funcionalidades Planificadas

- **Gestión de Rutas**: CRUD completo para trayectos
- **Información de Vuelos**: Códigos de aeropuerto, países, fechas
- **Gestión de Costos**: Costos de equipaje por trayecto
- **Integración con Publicaciones**: Base para asociar publicaciones con rutas específicas

## Tecnologías

- **Backend**: FastAPI (Python)
- **Base de Datos**: PostgreSQL
- **ORM**: SQLAlchemy

## Endpoints Planificados

| Método | Ruta | Descripción |
|--------|------|-------------|
| POST | `/routes` | Crear nuevo trayecto |
| GET | `/routes` | Listar trayectos |
| GET | `/routes/{id}` | Obtener trayecto específico |
| PATCH | `/routes/{id}` | Actualizar trayecto |
| DELETE | `/routes/{id}` | Eliminar trayecto |
| GET | `/routes/search` | Buscar trayectos por criterios |
| GET | `/routes/ping` | Health check |

## Modelo de Datos Planificado

### Route (Trayecto)
- `id`: Identificador único
- `flightId`: Identificador único del vuelo
- `sourceAirportCode`: Código del aeropuerto de origen
- `sourceCountry`: País de origen
- `destinyAirportCode`: Código del aeropuerto de destino
- `destinyCountry`: País de destino
- `bagCost`: Costo del equipaje para este trayecto
- `plannedStartDate`: Fecha/hora planificada de salida
- `plannedEndDate`: Fecha/hora planificada de llegada
- `createdAt`: Fecha de creación
- `updatedAt`: Fecha de última actualización

## Funcionalidades Adicionales

- **Búsqueda Avanzada**: Filtros por origen, destino, fechas, costos
- **Validación de Fechas**: Verificación de fechas coherentes
- **Gestión de Aeropuertos**: Catálogo de códigos IATA válidos

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