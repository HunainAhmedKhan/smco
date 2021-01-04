# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Product Extended',
    'version' : '1.0',
    'category': 'product',

    # Dependencies

    'depends' : ['product'],
    'license': 'OPL-1',

    
       
    # Views

    'data': [
        'views/product.xml',
    ],
    
    
    
       
    # Technical 
    
    'installable': True,
    'currency': 'EUR',
    'auto_install': False,
    'application': True,
}
