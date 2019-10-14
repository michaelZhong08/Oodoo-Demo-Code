from odoo import http
from odoo.http import request


class LibraryBookPortal(http.Controller):
    @http.route('/helloworld', auth="public", website=True)
    def helloworld(self, **kwargs):
        return request.render('library_website.helloworld')
    
    @http.route('/checkouts', auth='user', website=True)
    def checkouts(self, **kwargs):
        Checkout = request.env['library.checkout']
        checkouts = Checkout.search([])
        return request.render(
            'library_website.index',
            {'docs': checkouts})

    @http.route('/checkout/<model("library.checkout"):doc>',
        auth='user', # 默认值，但此处明确指定
        website=True)
    def checkout(self, doc, **kwargs):
        return http.request.render(
            'library_website.checkout',
            {'doc': doc})
