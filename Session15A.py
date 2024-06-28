# Database OOPS

import mysql.connector as db

class Database:

    def __init__(self):
        self.connection = db.connect(user="root", 
                        password="", 
                        host="127.0.0.1", 
                        database="gw2024pds",
                        )
        print("[Database] Connection Created")

        self.cursor = self.connection.cursor()
        print("[Database] Cursor Created")

    # insert/update/delete in DB
    def write(self, sql):
        print("[Database] SQL Statement - ", sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print("[Database] SQL Statement Executed Successfully...")

    # fetch data from DB
    def read(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result