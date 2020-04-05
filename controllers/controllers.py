# -*- coding: utf-8 -*-
from odoo import http

# class Addons/studiodesign(http.Controller):
#     @http.route('/addons/studiodesign/addons/studiodesign/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/studiodesign/addons/studiodesign/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/studiodesign.listing', {
#             'root': '/addons/studiodesign/addons/studiodesign',
#             'objects': http.request.env['addons/studiodesign.addons/studiodesign'].search([]),
#         })

#     @http.route('/addons/studiodesign/addons/studiodesign/objects/<model("addons/studiodesign.addons/studiodesign"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/studiodesign.object', {
#             'object': obj
#         })