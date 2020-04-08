# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProyectoMateriales(models.Model):
    _name = 'studiodesign.project.materiales'
    _rec_name = 'name'
    _description = 'Presupuesto de materiales para el pryecto'

    name = fields.Char(string="Nombre", required=False, )
    product_id = fields.Many2one(comodel_name="product.template", string="Producto", required=False, )
    product_qty = fields.Float(string="Cantidad",  required=False, )

    project_id = fields.Many2one(comodel_name="project.project", string="Projecto", required=False, )

class NewModule(models.Model):
    _inherit = 'project.project'

    lines_ids = fields.One2many(comodel_name="studiodesign.project.materiales", inverse_name="project_id", string="Lineas", required=False, )

class Stock(models.Model):
    _inherit = 'stock.picking'

    project_id = fields.Many2one(comodel_name="project.project", string="Proyecto", required=False, )
    user_id = fields.Many2one(comodel_name="res.users", string="Solicitante", required=False, )

