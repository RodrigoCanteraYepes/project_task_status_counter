# models/project.py
from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'
    
    # Campos de conteo individuales para cada estado - más fácil de trabajar en plantillas
    task_in_progress_count = fields.Integer(
        string='Conteo de Tareas En Progreso', 
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_changes_requested_count = fields.Integer(
        string='Conteo de Tareas con Cambios Solicitados',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_approved_count = fields.Integer(
        string='Conteo de Tareas Aprobadas',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_done_count = fields.Integer(
        string='Conteo de Tareas Completadas',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_canceled_count = fields.Integer(
        string='Conteo de Tareas Canceladas',
        compute='_compute_task_status_counts', 
        store=False
    )
    
    # Campos de porcentaje para tooltips
    task_in_progress_percent = fields.Char(
        string='Porcentaje En Progreso',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_changes_requested_percent = fields.Char(
        string='Porcentaje de Cambios Solicitados', 
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_approved_percent = fields.Char(
        string='Porcentaje Aprobado',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_done_percent = fields.Char(
        string='Porcentaje Completado',
        compute='_compute_task_status_counts',
        store=False
    )
    
    task_canceled_percent = fields.Char(
        string='Porcentaje Cancelado',
        compute='_compute_task_status_counts',
        store=False
    )
    
    @api.depends('task_ids.state')
    def _compute_task_status_counts(self):
        """Compute the count of tasks for each status including archived/closed tasks"""
        for project in self:
            # Get ALL tasks for this project, including archived/inactive ones
            all_tasks = self.env['project.task'].with_context(active_test=False).search([
                ('project_id', '=', project.id)
            ])
            
            if not all_tasks:
                project.task_in_progress_count = 0
                project.task_changes_requested_count = 0
                project.task_approved_count = 0
                project.task_done_count = 0
                project.task_canceled_count = 0
                project.task_in_progress_percent = "0%"
                project.task_changes_requested_percent = "0%"
                project.task_approved_percent = "0%"
                project.task_done_percent = "0%"
                project.task_canceled_percent = "0%"
                continue
            
            total_tasks = len(all_tasks)
            
            # Count tasks by state using filtered - matching your actual states
            in_progress_count = len(all_tasks.filtered(lambda t: t.state == '01_in_progress'))
            changes_requested_count = len(all_tasks.filtered(lambda t: t.state == '02_changes_requested'))
            approved_count = len(all_tasks.filtered(lambda t: t.state == '03_approved'))
            done_count = len(all_tasks.filtered(lambda t: t.state == '1_done'))
            canceled_count = len(all_tasks.filtered(lambda t: t.state == '1_canceled'))
            
            # Set counts
            project.task_in_progress_count = in_progress_count
            project.task_changes_requested_count = changes_requested_count
            project.task_approved_count = approved_count
            project.task_done_count = done_count
            project.task_canceled_count = canceled_count
            
            # Calculate percentages
            if total_tasks > 0:
                project.task_in_progress_percent = f"In Progress: {in_progress_count} ({round((in_progress_count / total_tasks) * 100)}%)"
                project.task_changes_requested_percent = f"Changes Requested: {changes_requested_count} ({round((changes_requested_count / total_tasks) * 100)}%)"
                project.task_approved_percent = f"Approved: {approved_count} ({round((approved_count / total_tasks) * 100)}%)"
                project.task_done_percent = f"Done: {done_count} ({round((done_count / total_tasks) * 100)}%)"
                project.task_canceled_percent = f"Canceled: {canceled_count} ({round((canceled_count / total_tasks) * 100)}%)"
            else:
                project.task_in_progress_percent = "0%"
                project.task_changes_requested_percent = "0%"
                project.task_approved_percent = "0%"
                project.task_done_percent = "0%"
                project.task_canceled_percent = "0%"
