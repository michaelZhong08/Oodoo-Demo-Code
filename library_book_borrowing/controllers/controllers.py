# -*- coding: utf-8 -*-
from odoo import http

# class LibraryBookBorrowing(http.Controller):
#     @http.route('/library_book_borrowing/library_book_borrowing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_book_borrowing/library_book_borrowing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_book_borrowing.listing', {
#             'root': '/library_book_borrowing/library_book_borrowing',
#             'objects': http.request.env['library_book_borrowing.library_book_borrowing'].search([]),
#         })

#     @http.route('/library_book_borrowing/library_book_borrowing/objects/<model("library_book_borrowing.library_book_borrowing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_book_borrowing.object', {
#             'object': obj
#         })