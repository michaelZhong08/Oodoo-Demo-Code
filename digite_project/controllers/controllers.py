# -*- coding: utf-8 -*-
from odoo import http

# class DigiteProject(http.Controller):
#     @http.route('/digite_project/digite_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/digite_project/digite_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('digite_project.listing', {
#             'root': '/digite_project/digite_project',
#             'objects': http.request.env['digite_project.digite_project'].search([]),
#         })

#     @http.route('/digite_project/digite_project/objects/<model("digite_project.digite_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('digite_project.object', {
#             'object': obj
#         })