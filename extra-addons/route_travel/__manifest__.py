# -*- coding: utf-8 -*-
{
    'name': 'Route_travel',
    'version': '16.0.0.1',
    'summary': """ Route_travel Summary """,
    'author': 'Andresow',
    'category': 'fleet',
    'depends': ['base', 'fleet','sale'],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
        "views/route_fleet_views.xml",
        "views/route_travel_state_views.xml"
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
