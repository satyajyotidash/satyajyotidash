import sqlite3


def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn
   

con=create_connection("C:\sqlite\db\pythonsqlite1.db")
print(con)
