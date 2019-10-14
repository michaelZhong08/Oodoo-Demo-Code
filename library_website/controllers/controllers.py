# -*- coding: utf-8 -*-
from odoo import http

# class LibraryWebsite(http.Controller):
#     @http.route('/library_website/library_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_website/library_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_website.listing', {
#             'root': '/library_website/library_website',
#             'objects': http.request.env['library_website.library_website'].search([]),
#         })

#     @http.route('/library_website/library_website/objects/<model("library_website.library_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_website.object', {
#             'object': obj
#         })