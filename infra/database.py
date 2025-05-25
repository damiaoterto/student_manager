import os
import sqlite3

class Database:
    def __init__(self):
        self._cwd = os.getcwd()
        self._connection = sqlite3.connect(f'{self._cwd}/db.sqlite')
        self._cursor = self._connection.cursor()
        self._tables = [
            """
                CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
                );
            """
        ]
        self._create_tables()

    def get_cursor(self):
        return self._cursor

    def _create_tables(self):
        for table in self._tables:
            self._cursor.execute(table)
            self._connection.commit()

    def select_all(self, table:str, column=None):
        if column is None:
            column = ["*"]

        cols = ",".join(column)
        result = self._cursor.execute(f"SELECT {cols} FROM {table}")
        return result.fetchall()

    def insert_item(self, table: str, columns: list[str], params: slice):
        cols = ','.join(columns)
        query_params = " ?" * len(columns)
        values = query_params.split()

        query = f'INSERT INTO {table} ({cols}) VALUES ({','.join(values)})'
        self._cursor.execute(query, params)
        self._connection.commit()

    def delete_item(self, table: str, idx):
        query = f'DELETE FROM {table} WHERE id = ?'
        self._cursor.execute(query, (idx,))
        self._connection.commit()

    def close(self):
        self._connection.close()