# -*- coding: utf-8 -*-
# from odoo import http


# class Smc(http.Controller):
#     @http.route('/smc/smc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smc/smc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('smc.listing', {
#             'root': '/smc/smc',
#             'objects': http.request.env['smc.smc'].search([]),
#         })

#     @http.route('/smc/smc/objects/<model("smc.smc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smc.object', {
#             'object': obj
#         })
