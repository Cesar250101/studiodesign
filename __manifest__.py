# -*- coding: utf-8 -*-
{
    'name': "studiodesign",

    'summary': """
        localización de Odoo  para la empresa Studio Design""",

    'description': """
        1.-Agrega a proyectos lista de materiales standar
    """,

    'author': "Method",
    'website': "http://www.openmethod.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','project','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/proyetos_listamatriales.xml',
        'reports/proyetos_listamatriales_template.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
