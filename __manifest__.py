{
    'name': 'Contador de Estado de Tareas de Proyecto',
    'version': '18.0.1.0.0',
    'category': 'Proyecto',
    'summary': 'Mostrar contadores de estado de tareas en la vista kanban de proyectos',
    'description': '''
        Este módulo añade insignias de conteo de estado a las tarjetas kanban de proyectos mostrando
        el conteo de tareas para cada estado en el proyecto usando los patrones de UI
        existentes de Odoo.
    ''',
    'author': 'Tu Empresa',
    'website': 'https://www.tuempresa.com',
    'depends': ['project'],
    'data': [
        'views/project_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'project_task_status_counter/static/src/css/status_counts.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
