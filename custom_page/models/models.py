# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class custom_page(models.Model):
#     _name = 'custom_page.custom_page'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class testmodel(models.Model):
    _name='test model'

    name=fields.Char()