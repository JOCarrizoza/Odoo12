# -*- coding: utf-8 -*-
# Copyright © 2019 - All Rights Reserved
# Author      Business SYS Developers México.

{
    'name': 'CarWash with logo POS',
    'summary': 'Logo For Every Point of Sale',
    'description': """ It can be implemented in any car wash, includes post_log and printing of car data on the ticket """,
    'author': 'JO Carrizoza',
    'license': 'AGPL-3',
    'category' : 'Point Of Sale',
    'version' : '12.1',
    'depends': [
        'base',
        'point_of_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/car.brands.csv',
        'data/car.models.csv',
        'views/res_partner_views.xml',
        'views/car_brand_views.xml',
        'views/car_model_views.xml',
        'views/car_color_views.xml',
        'views/pos_image_view.xml',
        'views/pos_config_view.xml',        
    ],
    'qweb': [
        'static/src/xml/pos.xml',
        'static/src/xml/pos_ticket_view.xml',
        'static/src/xml/pos_client_view.xml',
    ],
    'application': True,
    #'auto_install': False,
}
