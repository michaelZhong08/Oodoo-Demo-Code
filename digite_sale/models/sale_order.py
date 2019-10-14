from odoo import fields,models,api
import datetime as dt
import odoo.tools.date_utils
#from dateutil.parse import parse

class saleorder(models.Model):
    _inherit='sale.order'
    
    digite_pydate=fields.Date(string='py date',readonly=True,compute='_compute_pydate',required=True,store=True)
    digite_pydateold=fields.Date()

    def _default_paymentid(self):
        #print('test default func')
        return self.env['account.payment.term'].search([],limit=1)
    payment_term_id=fields.Many2one('account.payment.term',default=_default_paymentid)
    payment_term_id_1=fields.Many2one('account.payment.term',default=_default_paymentid)

    payratio=fields.Float(string='Pay Ratio(%)')
    paydatespan=fields.Integer(compute='_compute_paytimespan')

    @api.depends('payment_term_id','validity_date')
    def _compute_pydate(self):
        DATE_FORMAT='%Y-%m-%d'
        for record in self:
            if record.payment_term_id:
                if record.validity_date:
                    this_payment_term_line=self.env['account.payment.term.line'].search([('payment_id','=',record.payment_term_id.id)],limit=1)#record.payment_term_id
                    #paydate=self.env['sale.order'].search([('id','=','3')],limit=1).digite_pydate
                    #if paydate:
                        #print((odoo.fields.Date.today()-paydate).days)
                        #record.digite_pydateold=paydate
                    record.digite_pydate=(record.validity_date +  dt.timedelta(days=this_payment_term_line.days)).strftime(DATE_FORMAT)#dt.datetime.strptime(record.validity_date, DATE_FORMAT)
                    #print('this_payment_term_line:')
                    #print(str(this_payment_term_line.id))
                    #print(self.env['account.payment.term'].browse(3).id)

    @api.constrains('payment_term_id')
    def _check_paymentid_notnull(self):
        for record in self:
            if not record.payment_term_id:
                raise exceptions.ValidationError("[payment_term_id] not null!")
    
    @api.multi
    def write(self,vals):
        #if vals['payment_term_id'] and vals['payment_term_id_1']:
            #vals['payment_term_id']=vals['payment_term_id_1']
        #print('model write test -- ......\n')
        #print(vals)
        super().write(vals)
        return True

    @api.onchange('payment_term_id_1')
    def _onchange_paymentid(self):
        for record in self:
            if record.payment_term_id_1:
                record.payment_term_id=record.payment_term_id_1

    @api.depends()
    def _compute_paytimespan(self):
        for record in self:
            paydate = self.env['sale.order'].search([('id', '=', str(record.id))], limit=1).digite_pydate
            thedate = None
            if paydate:
                thedate = paydate
            else:
                pass
            record.paydatespan = (odoo.fields.Date.today()-thedate).days
