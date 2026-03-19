{
    'name': 'Odoo N Extension',
    'version': '18.0.1.0.0',
    'summary': 'Module for extending Sale Order with custom fields and logic',
    'author': 'N',
    'category': 'Sales',
    'depends': ['sale', 'hr'],
    'data': [
        'views/sale_order_views.xml',
        'report/sale_report_templates.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
