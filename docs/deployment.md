# Vista de Despliegue

Esta vista describe cómo los componentes del sistema se despliegan en el clúster de Kubernetes y cómo se conectan entre sí.

## Descripción

Cada microservicio (users, posts, routes, offers) se despliega en su propio pod dentro del clúster K8s. Cada uno expone un servicio de tipo NodePort para acceso externo y se conecta a su propia base de datos PostgreSQL a través de un servicio ClusterIP. Todas las bases de datos usan el puerto 5432.

- Los servicios NodePort exponen los microservicios en los puertos 30000, 30001, 30002 y 30003 respectivamente.
- Cada microservicio se comunica únicamente con su propia base de datos.
- El acceso externo se realiza a través de los puertos NodePort definidos.

## Modelo de despliegue y red

El siguiente diagrama PlantUML representa la vista de despliegue y red del sistema:

```plantuml
!include diagrams/networks.puml
```

El archivo `networks.puml` se encuentra en `docs/diagrams/` y contiene el modelo de red generado con PlantUML.

## Archivos relacionados
- `docs/diagrams/networks.puml`: Diagrama de red y despliegue (PlantUML)
- `k8s/`: Manifiestos de Kubernetes para todos los servicios y bases de datos
