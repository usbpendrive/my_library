{
    'name': 'Odoo My Library Module',
    'summary': 'Manage Books Easily',
    'description': """
    Manage your books library easily using this module.
    """,
    'author': 'Fernando',
    'license': 'LGPL-3',
    'application': True,
    'version': '12.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml',
    ]
}
