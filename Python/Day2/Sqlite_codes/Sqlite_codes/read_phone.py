import sqlite3
import xlwt

def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

def read_contact(conn):
    wb = xlwt.Workbook() 
    sheet1 = wb.add_sheet('mycontacts') 
    sheet1.write(0, 0, 'Name')
    sheet1.write(0, 1, 'Phone')
    sheet1.write(0, 2, 'Email-ID')
    sheet1.write(0, 3, 'City')
    sheet1.write(0, 4, 'Country')
    sql = ''' select * from phoneBook'''
    cur = conn.cursor()
    cur.execute(sql)
    res=cur.fetchall()#[(),(),()]
    count=1
    for d in res:
        print(d[0],"\t",d[1],"\t",d[2],"\t",d[3],"\t",d[4])
        sheet1.write(count,0,d[0])
        sheet1.write(count,1,d[1])
        sheet1.write(count,2,d[2])
        sheet1.write(count,3,d[3])
        sheet1.write(count,4,d[4])
        count=count+1
    wb.save("C:\\Users\\madhu\\Desktop\\contacts.xls")
   
   

database = "C:\sqlite\db\pythonsqlite1.db"
conn = create_connection(database)

read_contact(conn)
        

        
