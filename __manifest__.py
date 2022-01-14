{
    'name': 'Sales Tags',
    'version': '13.0.0.1',
    'author': 'Ajay',
    'depends': ['base', 'account', 'sale'],
    'data': [ 
        'security/ir.model.access.csv',
        'views/sales_tags.xml',
        'views/sample_menu.xml',
        'views/sales_order_inherit.xml'     
    ],
    'sequence': '4',
    'application': True,



}