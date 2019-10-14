# -*- coding: utf-8 -*-
from odoo import http

# class TurorialTheme(http.Controller):
#     @http.route('/turorial_theme/turorial_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/turorial_theme/turorial_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('turorial_theme.listing', {
#             'root': '/turorial_theme/turorial_theme',
#             'objects': http.request.env['turorial_theme.turorial_theme'].search([]),
#         })

#     @http.route('/turorial_theme/turorial_theme/objects/<model("turorial_theme.turorial_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('turorial_theme.object', {
#             'object': obj
#         })