from odoo import models,fields,api,exceptions

class Project(models.Model):
    _name='digiteproject.project'
    _description='Digite Project'
    _inherit=['mail.thread','mail.activity.mixin']

    project_num=fields.Char('Project Number')
    project_name=fields.Char('Project Name')
    project_customerid=fields.Integer('Customer ID')
    project_customername=fields.Char('Customer Name')
    #--------------------------------------------
    @api.model
    def _default_stage(self):
        Stage = self.env['digiteproject.project.stage']
        return Stage.search([], limit=1)
    @api.model
    def _group_expand_stage_id(self, stages, domain, order):
        return stages.search([], order=order)

    stage_id = fields.Many2one(
        'digiteproject.project.stage',
        default=_default_stage,
        group_expand='_group_expand_stage_id')
    state = fields.Selection(related='stage_id.state')
    #--------------------------------------------
    priority = fields.Selection(
        [('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')],
        'Priority',
        default='1')
    kanban_state = fields.Selection(
        [('normal', 'In Progress'),
        ('blocked', 'Blocked'),
        ('done', 'Ready for next stage')],
        'Kanban State',
        default='normal')
    kanban_color = fields.Integer('Color Index', default=0)
    #--------------------------------------------