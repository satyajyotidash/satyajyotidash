import sqlite3
def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn, sqlQuery):
    c = conn.cursor()
    c.execute(sqlQuery)
    conn.commit()

database = "C:\sqlite\db\pythonsqlite1.db"
conn = create_connection(database)

sqlQuery = """CREATE TABLE IF NOT EXISTS phoneBook (
                                        name text PRIMARY KEY,
                                        phone integer NOT NULL,
                                        email text NOT NULL,
                                        city text NOT NULL,
                                        Country text NOT NULL
                                        
                                    ); """


if conn is not None:
    create_table(conn, sqlQuery)
else:
    print("Error! cannot create the database connection.")

conn.close()
