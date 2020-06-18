# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProyectoMateriales(models.Model):
    _name = 'studiodesign.project.materiales'
    _rec_name = 'name'
    _description = 'Presupuesto de materiales para el pryecto'

    name = fields.Char(string="Nombre", required=False, )
    product_id = fields.Many2one(comodel_name="product.template", string="Producto", required=False, domain = "[('x_mis_productos','=',True),('purchase_ok','=',True)]")
    product_qty = fields.Float(string="Cantidad",  required=False, )
    project_id = fields.Many2one(comodel_name="project.project", string="Projecto", required=False, )
    standard_price=fields.Float(string='Costo',related="product_id.standard_price")
    sub_total = fields.Float(string='Subtotal', compute="_subtotalcosto")

    @api.one
    @api.depends('standard_price','product_qty')
    def _subtotalcosto(self):
        self.sub_total=self.product_qty*self.standard_price

class NewModule(models.Model):
    _name='studiodesign.project'
    _inherit = ['project.project','mail.thread', 'mail.activity.mixin']

    lines_ids = fields.One2many(comodel_name="studiodesign.project.materiales", inverse_name="project_id", string="Lineas", required=False, )

class Stock(models.Model):
    _inherit = 'stock.picking'

    analytic_account_id = fields.Many2one(string='Proyecto',comodel_name='account.analytic.account',)
    user_id = fields.Many2one(comodel_name="res.users", string="Solicitante", required=False, )

    @api.onchange('project_id')
    def _onchange_project_id(self):
        for i in self.move_lines:
            i.analityc_account_id=self.project_id
        return True

class NewModule(models.Model):
    _inherit = 'stock.move'

    analytic_account_id = fields.Many2one(string='Analytic Account',comodel_name='account.analytic.account',
                                          related="picking_id.analytic_account_id")
