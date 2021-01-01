# -*- coding: utf-8 -*-

from odoo import models, fields, api



class smc(models.Model):
    _inherit = 'product.product'

    def name_get(self):

        res = []
        for rec in self:
            res.append((rec.id, '%s : %s' % (rec.name, rec.article_no)))
        return res

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100):

        if args is None:
            print("after")
            args = []
        domain = args + ['|', '|', ('finish_no', operator, name), ('article_no', operator, name),
                         ('name', operator, name)]
        return super(smc, self).search(domain, limit=limit).name_get()












#

#








