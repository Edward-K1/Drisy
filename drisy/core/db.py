import sqlite3

from collections import OrderedDict

from .schema import table_schema
from .globals import db_path


class DrisyDb:
    def __init__(self):
        self.db_path = db_path
        self.db_conn = sqlite3.connect(db_path)

    def create_table(self, schema):
        query = f"CREATE TABLE IF NOT EXISTS {schema['name']}({self.get_table_definition(schema)})"
        self.execute_query(query)

    def create_tables(self):
        for schema in table_schema:
            self.create_table(schema)

    def recreate_tables(self):
        for schema in table_schema:
            self.drop_table(schema['name'])
            query = f"CREATE TABLE {schema['name']}({self.get_table_definition(schema)})"
            self.execute_query(query)

    def drop_table(self, name):
        query = f"DROP TABLE IF EXISTS {name}"
        self.execute_query(query)

    def get_table_definition(self, schema):
        columns = ','.join([f'{k} {v}' for (k, v) in schema['fields'].items()])
        constraints = ','.join(schema['constraints'])
        definition = ','.join((columns, constraints))
        return definition

    def execute_query(self, sql_query, params=None):
        if params:
            with self.db_conn as connection:
                cursor = connection.cursor()
                results = cursor.execute(sql_query, params)
        else:
            with self.db_conn as connection:
                cursor = connection.cursor()
                results = cursor.execute(sql_query)

        return results

    def save_from_dict(self, drive_listing):
        self.create_tables()
        for info in drive_listing:
            mapping = self.map_file_info(info)
            self.save_user(mapping)
            self.save_file_info(mapping)

    def save_user(self, info_map):
        username = info_map.pop('username')
        email = info_map.pop('uem')
        query = f"INSERT INTO owners(uem, username)VALUES(?,?)"
        try:
            # a unique constraint exception is  being thrown
            # here since a user's details are stored when storing
            # metadata of their first file
            self.execute_query(query, params=(email, username))

        except sqlite3.IntegrityError as ex:
            print(str(ex))

    def save_file_info(self, info_map):
        placeholders = ','.join(list('?' * len(info_map)))
        columns = ','.join(info_map.keys())
        query = f"INSERT INTO files({columns}) VALUES({placeholders})"
        try:
            self.execute_query(query, params=(tuple(info_map.values())))
            
        except sqlite3.Error as ex:
            print(str(ex))

    def map_file_info(self, info):
        global_map = {
            'username': info['owners'][0]['displayName'],
            'uem': info['owners'][0]['emailAddress'],
            'gid': info['id'],
            'filename': info['name'],
            'mimetype': info['mimeType'],
            'weblink': info['webViewLink'],
            'created_at': info['createdTime'],
            'updated_at': info['modifiedTime'],
            'viewedbyme': info['viewedByMe'],
            'modifiedbyme': info['modifiedByMe'],
            'owner': info['owners'][0]['emailAddress'],
        }

        return OrderedDict(global_map)

    def tables_exist(self):
        query = "SELECT * FROM owners LIMIT 1"
        status = False

        try:
            result = self.execute_query(query)
            status = True
        except sqlite3.Error:
            pass
        return status


    def get_dict_entries(self):
        query = "select f.*, usr.username from files f, owners usr where f.owner=usr.uem"
        results = self.execute_query(query)
        column_names = [c[0] for c in results.description]
        dict_list = [dict(zip(column_names, row)) for row in results.fetchall()]
        return dict_list
        
