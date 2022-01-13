{
    'name': 'Sales Tags',
    'author': 'Ajay',
    'version': '13.0.1',

    #any module necessary for this one to work correctly
    'depends': ['account', 'base', 'sale'],

    #always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sales_tags.xml'
    ],
    'sequence': '1',
    'application': True,

}