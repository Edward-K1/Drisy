#
# Well, this schema file is a mess.
# Seemed like a great idea at the time :)
#
# First see the problem it solves in the DB file before editing
#

from collections import OrderedDict

table_schema = [{
    'name':'owners',
    'fields':
    OrderedDict([('uem', 'VARCHAR(100)'),
                 ('username', 'VARCHAR(50) NOT NULL')]),
    'constraints': ('PRIMARY KEY(uem)', )
}, {
    'name':'files',
    'fields':
    OrderedDict([('id', 'INTEGER'), ('gid', 'VARCHAR(200) UNIQUE'),
                 ('filename', 'TEXT'), ('mimetype', 'VARCHAR(100)'),
                 ('weblink', 'VARCHAR(100)'), ('created_at', 'DATETIME'),
                 ('updated_at', 'DATETIME'), ('viewedbyme', 'BOOLEAN'),
                 ('modifiedbyme', 'BOOLEAN'), ('tags', 'TEXT'),
                 ('owner', 'VARCHAR')]),
    'constraints':
    ('PRIMARY KEY(id)',
     'FOREIGN KEY(owner) REFERENCES owners(uem) ON DELETE CASCADE')
}, {
    'name':'tags',
    'fields':
    OrderedDict([('id', 'INTEGER'), ('name', 'VARCHAR(50) UNIQUE'),
                 ('description', 'VARCHAR(100)')]),
    'constraints': ('PRIMARY KEY(id)', )
}]
