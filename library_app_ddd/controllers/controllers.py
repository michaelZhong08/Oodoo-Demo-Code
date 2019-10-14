# -*- coding: utf-8 -*-
from odoo import http
from psycopg2 import IntegrityError

# class LibraryApp(http.Controller):
#     @http.route('/library_app/library_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_app/library_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_app.listing', {
#             'root': '/library_app/library_app',
#             'objects': http.request.env['library_app.library_app'].search([]),
#         })

#     @http.route('/library_app/library_app/objects/<model("library_app.library_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_app.object', {
#             'object': obj
#         })

class MyUsernameController(http.Controller):
  @http.route('/myusername/create', type='http', auth='public', website=True)
  def create(self, **kwargs):
    if http.request.httprequest.method == 'POST':
      username = kwargs.get('username', None)
      try:
        http.request.env['my.username'].create({
            'username': username
        })
        return http.request.render('library_app.ok', {
            'username': username
        })
      except IntegrityError:
        # IntegrityError handler
        http.request._cr.rollback()
        return http.request.render('library_app.error')
    return http.request.render('library_app.home')