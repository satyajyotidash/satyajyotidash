import sqlite3

def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

database = "C:\sqlite\db\pythonsqlite.db"
conn = create_connection(database)
sql = ''' select * from myPhoneBook'''
cur = conn.cursor()
cur.execute(sql)
data=cur.fetchall()


import xlrd 
from xlutils.copy import copy

rwb = xlrd.open_workbook("data.xls")
wwb = copy(rwb)

s = wwb.get_sheet(1)
s.write(0,0,"NAME")
s.write(0,1,"PHONE NUMBER")
s.write(0,2,"EMAIL-ID")
s.write(0,3,"CITY")

count=1
for contact in data:
    s.write(count,0,contact[0])
    s.write(count,1,contact[1])
    s.write(count,2,contact[2])
    s.write(count,3,contact[3])
    count=count+1
    

wwb.save('data.xls')


