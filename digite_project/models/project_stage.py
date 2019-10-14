from odoo import models,fields,api

class Project_Stage(models.Model):
    _name='digiteproject.project.stage'
    _description='Digite Proect Stage'
    _order='sequence,name'

    name = fields.Char()
    sequence = fields.Integer(default=10)
    #fold = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [('new', 'Stage 1'),
        ('open', 'Stage 2'),
        ('done', 'Stage 3'),
        ('cancel', 'Cancelled')],
        default='new',
    )
    