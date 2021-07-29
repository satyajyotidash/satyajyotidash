import sqlite3
def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

def add_project(conn, project):
    sql = ''' INSERT INTO projects(id,name,begin_date,end_date)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql,project)
    conn.commit()
   
database = "C:\sqlite\db\pythonsqlite1.db"
conn = create_connection(database)
project1 = (101,'Cool App with SQLite & Python', '2020-01-01', '2020-01-30')
project2 = (102,'Cool App with SQLite & Java', '2019-01-01', '2019-01-30')
project3 = (103,'Cool App with SQLite & .net', '2018-01-01', '2018-01-30')
project4 = (104,'Cool App with SQLite & Perl', '2017-01-01', '2017-01-30')
project5 = (105,'Cool App with SQLite & R', '2016-01-01', '2016-01-30')
project6 = (106,'Cool App with SQLite & Go', '2015-01-01', '2015-01-30')
project7 = (107,'Cool App with SQLite & Spark', '2021-01-01', '2021-01-30')
project8 = (108,'Cool App with SQLite & CPP', '2022-01-01', '2022-01-30')

add_project(conn, project1)
add_project(conn, project2)
add_project(conn, project3)
add_project(conn, project4)
add_project(conn, project5)
add_project(conn, project6)
add_project(conn, project7)
add_project(conn, project8) 
conn.close()
        
