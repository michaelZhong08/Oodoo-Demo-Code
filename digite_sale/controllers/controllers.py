# -*- coding: utf-8 -*-
from odoo import http

# class DigiteSale(http.Controller):
#     @http.route('/digite_sale/digite_sale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/digite_sale/digite_sale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('digite_sale.listing', {
#             'root': '/digite_sale/digite_sale',
#             'objects': http.request.env['digite_sale.digite_sale'].search([]),
#         })

#     @http.route('/digite_sale/digite_sale/objects/<model("digite_sale.digite_sale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('digite_sale.object', {
#             'object': obj
#         })