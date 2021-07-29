import sqlite3
def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn, sqlQuery):
    c = conn.cursor()
    c.execute(sqlQuery)
    conn.commit()
 
conn = create_connection("C:\sqlite\db\pythonsqlite1.db")

sqlQuery = ''' CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); '''

if conn is not None:
       
    create_table(conn, sqlQuery)

else:
    print("Error! cannot create the database connection.")

conn.close()
