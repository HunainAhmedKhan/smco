# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'smc_customization.smc_customization'

    article_no = fields.Char()
    finish_no = fields.Char()
    sqm_box = fields.Float(string="SQM/Box")
    pcs_box = fields.Integer(string="PCS/Box")
    show_bol=fields.Boolean("Show in SO")



class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'saleorder.customization'

    address = fields.Char("Address",related="partner_id.street")
    mobile_no = fields.Char("Mobile No",related="partner_id.mobile")
    email_id = fields.Char(string="Email Id",related="partner_id.email")
    architect = fields.Char(string="Architect")
    project_description=fields.Text("Project Description")




class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _description = 'saleorder.customization'

    number = fields.Integer(
        compute='_compute_get_number',
        store=True,
    )

    article_no = fields.Char("Article#",related="product_id.article_no")
    finish_no = fields.Char("Finish",related="product_id.finish_no")
    total_sqm = fields.Char(string="Total SQM",compute="_onchange_product_uom_qty")
    total_pcs = fields.Char(string="Total Pcs",compute="_onchange_product_uom_qty")

    @api.depends('product_uom_qty')
    def _onchange_product_uom_qty(self):
        for i in self:
            i.total_sqm=i.product_uom_qty*i.product_id.sqm_box
            i.total_pcs=i.product_uom_qty*i.product_id.pcs_box



    @api.depends('sequence', 'order_id')
    def _compute_get_number(self):
        for order in self.mapped('order_id'):
            number = 1
            for line in order.order_line:
                line.number = number
                number += 1
