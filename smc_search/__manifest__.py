# -*- coding: utf-8 -*-
{
    'name': "SMC search by Article No/Finish",

    'summary': """
        Implement some internal customization""",

    'description': """
        product which search by its article number and product will be shown with name and finish
    """,

    'author': "Tabeer Aslam Odoo Consultant",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
