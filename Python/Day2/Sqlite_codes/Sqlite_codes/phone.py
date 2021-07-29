import sqlite3
def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn


    



database = "C:\sqlite\db\pythonsqlite.db"

sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS myPhoneBook (
                                        name text PRIMARY KEY,
                                        phone integer NOT NULL,
                                        email text NOT NULL,
                                        city text NOT NULL
                                    ); """

conn = create_connection(database)
c = conn.cursor()
c.execute(sql_create_projects_table)

    



