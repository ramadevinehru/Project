import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456789',
            database='placement'
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
