{
    'name': 'ERD DE',
    'summary': 'Change The Odoo List view On the fly without any technical knowledge',
    'version': '1.0',
    'category': 'Web',
    'description': """
        
    """,
    'author': "tyt",
    'depends': ['web'],
    'data': ['views/templates.xml',
             'security/show_fields_security.xml',
             'security/ir.model.access.csv'],
    'price': 99,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
    'qweb': ['static/src/xml/base.xml'],
    'images': [
        
    ],
}
