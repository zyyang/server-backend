# Copyright <2011> <Daniel Reis, Maxime Chambreuil, Savoir-faire Linux>
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    'name': 'External Database Source - MySQL',
    'version': '12.0.1.0.0',
    'category': 'Tools',
    'author': "Daniel Reis, "
              "LasLabs, "
              "Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/server-backend',
    'license': 'LGPL-3',
    'depends': [
        'base_external_dbsource_sqlite',
    ],
    'external_dependencies': {
        'python': [
            'sqlalchemy',
            'MySQLdb',
        ],
    },
    'demo': [
        'demo/base_external_dbsource.xml',
    ],
    'installable': True,
}
