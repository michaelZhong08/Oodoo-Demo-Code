from odoo import http

class MyClass(http.Controller):

    @http.route('/myclass/jstestView',auth="public", website=True)
    def jstest(self,**kwargs):
        return http.request.render(
            'petstore.jstest_template'
            )