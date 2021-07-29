import sqlite3

def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

def add_contact(conn, contact):
    sql = ''' INSERT INTO phoneBook(name,phone,email,city,Country)
    VALUES(?,?,?,?,?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql,contact)
        conn.commit()
    except(sqlite3.IntegrityError) as err:
        print(err)
        print("contact exist for ",contact[0])
    
        
database = "C:\sqlite\db\pythonsqlite1.db"
conn = create_connection(database)

myPh={"Roger":[999908999,"Roger@gmail.com","London","England"],
      "Smith1":[898398787,"Smith@yahoo.com","Munich","Germany"],
      "David1":[909000999,"David@hotmail.com","Rome","Italy"],
      "John1":[8987877878,"John.er@live.com","Madrid","Spain"],
      "Josh1":[8897897870,"Josh@rediff.com","paris","France"],
      "will":[78687686,"Roger@gmail.com","London","England"],
      "annie1":[898398787,"Smith@yahoo.com","Munich","Germany"],
      "rafter1":[987868686,"David@hotmail.com","Rome","Italy"],
      "naman1":[4546456655,"John.er@live.com","Madrid","Spain"],
      "joy1":[8897897870,"Josh@rediff.com","paris","France"]}


for name,details in myPh.items():
    cont=(name,details[0],details[1],details[2],details[3])
    add_contact(conn,cont)

        
conn.close()
        
