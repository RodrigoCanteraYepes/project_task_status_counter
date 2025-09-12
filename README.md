# Contador de Estado de Tareas de Proyecto

Módulo de Odoo que muestra insignias de conteo de estado de tareas en las tarjetas kanban de proyectos.

## Características

- Muestra insignias de conteo para cada estado de tarea en las tarjetas de proyecto
- Cuenta TODAS las tareas (incluyendo completadas/archivadas)
- Insignias codificadas por color con tooltips mostrando porcentajes

## Instalación

1. Copiar módulo a tu directorio de addons de Odoo
2. Actualizar Lista de Aplicaciones
3. Instalar "Project Task Status Counter"

## Estados de Tarea Soportados

- `01_in_progress` - Insignia azul
- `02_changes_requested` - Insignia naranja  
- `03_approved` - Insignia verde azulado
- `1_done` - Insignia verde
- `1_canceled` - Insignia roja

## Requisitos

- Odoo 17.0+
- módulo project

## Estructura de Archivos

```
project_task_status_counter/
├── __manifest__.py
├── models/project.py
├── views/project_views.xml
└── static/src/css/status_counts.css
```
