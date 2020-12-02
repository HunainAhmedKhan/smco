# -*- coding: utf-8 -*-
# from odoo import http


# class SmcCustomization(http.Controller):
#     @http.route('/smc_customization/smc_customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/smc_customization/smc_customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('smc_customization.listing', {
#             'root': '/smc_customization/smc_customization',
#             'objects': http.request.env['smc_customization.smc_customization'].search([]),
#         })

#     @http.route('/smc_customization/smc_customization/objects/<model("smc_customization.smc_customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('smc_customization.object', {
#             'object': obj
#         })
