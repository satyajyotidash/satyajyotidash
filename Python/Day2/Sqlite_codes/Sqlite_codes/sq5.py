import sqlite3
def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

def read_data_table(conn):
    sql =" select * from projects "
    cur = conn.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    #print(data)#[(,,,),(,,,),(),(),(),(),(),()]
    
    for val in data:
        print(val[0],"\t",val[1],"\t",val[2],"\t",val[3])
   

database = "C:\sqlite\db\pythonsqlite1.db"
conn = create_connection(database)
read_data_table(conn)
        
conn.close()
        
