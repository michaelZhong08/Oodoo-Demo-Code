# -*- coding: utf-8 -*-
from odoo import http

# class Petstore(http.Controller):
#     @http.route('/petstore/petstore/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/petstore/petstore/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('petstore.listing', {
#             'root': '/petstore/petstore',
#             'objects': http.request.env['petstore.petstore'].search([]),
#         })

#     @http.route('/petstore/petstore/objects/<model("petstore.petstore"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('petstore.object', {
#             'object': obj
#         })