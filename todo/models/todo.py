from odoo import fields,models,api

class TodoMain(models.Model):
    _name='todo.main'
    _description='To do app main'

    user_id=fields.Many2one(
        'res.users',
        default=lambda s:s.env.uid
    )
    record_date=fields.Date(
        default=lambda s:fields.Date.today()
    )
    state=fields.Selection(
        [('new', 'Draft'),
        ('open', 'Open'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')],
        default='open',
    )
    line_ids=fields.One2many(
        'todo.line',
        'main_id',
        string='To do Items'
    )
    completeness=fields.Float(string='WanChengDu')

    @api.multi
    def btn_method(self):
        _curusername=self.env['res.partner'].search([('id','=',self.env.user.partner_id.id)],limit=1).name
        print(self.env.user.partner_id.name)
        print(_curusername)
        #self.env.cr.execute('SELECT * FROM RES_PARTNER')
        #print(self.env.cr.dictfetchall())

class TodoLine(models.Model):
    _name='todo.line'
    _description='To do app line'
    
    name=fields.Char(sting='To do Item')
    finish_date=fields.Date(
        string='Finish Time',
        default=''
    )
    is_done=fields.Boolean(sting='Is done?')
    main_id=fields.Many2one(
        'todo.main',
    )
