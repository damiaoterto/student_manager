import os
import sqlite3

class Database:
    def __init__(self):
        self._cwd = os.getcwd()
        self._connection = sqlite3.connect(f'{self._cwd}/db.sqlite')
        self._cursor = self._connection.cursor()

    def get_cursor(self):
        return self._cursor

    def execute_query(self, query, params=None):
        self._cursor.execute(query, params)

    def insert_item(self, table: str, columns: list[str], params: slice):
        columns = ','.join(columns)
        query_params = "?" * len(columns)
        values = query_params.split('')
        query = f'INSERT INTO {table} {columns} VALUES ({','.join(values)})'
        self._cursor.execute(query, params)
        self._connection.commit()

    def close(self):
        self._connection.close()