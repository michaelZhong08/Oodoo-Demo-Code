from odoo import fields,models

class Book(models.Model):
    _inherit='library.book'
    is_available=fields.Boolean('Is Available?')
    isbn=fields.Char(help="Val Default: isbn")
    publisher_id=fields.Many2one(index=True)