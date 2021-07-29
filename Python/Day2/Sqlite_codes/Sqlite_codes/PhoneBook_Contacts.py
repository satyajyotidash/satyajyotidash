import sqlite3

def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

def add_contact(conn, data):
    sql = ''' INSERT INTO phoneBook(name,phone,email,city,Country)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()

def delFromTable(conn, data):
    sql = ''' DELETE FROM phoneBook where name=?'''
    cur = conn.cursor()
    cur.execute(sql,(data,))
    conn.commit()


print("PHONE BOOK CONTACT MANAGEMENT")
myPhoneBook={}

def loadPhoneBook(conn,myPhoneBook):
    sql = ''' select * from phoneBook'''
    cur = conn.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    for row in data:
        myPhoneBook[row[0]]=[row[1],row[2],row[3],row[4]]

    

database = "C:\sqlite\db\pythonsqlite1.db"
conn = create_connection(database)

loadPhoneBook(conn,myPhoneBook)

while True:
    print("Number of Contacts in myPhoneBook = ",len(myPhoneBook))
    print("1 : Add Contact")
    print("2 : Display Contacts")
    print("3 : Serach Contact")
    print("4 : Delete Conatct")
    print("5 : Edit Contact")
    print("0 : exit")
    choice=int(input("enter your choice"))
    print("choice = ",choice)

    if(choice == 1):
        print("Adding new contact")
        name=input("enter the name of contact to be added")
        if name in myPhoneBook:
            print("contact exist with sam name in my phone book")
            print("duplicate contacts can't be added")
        else:
            print("contact doesn't exist with this name")
            print("please enter other details")
            ph=int(input("enter phone number"))
            email=input("enter email-ID")
            city=input("enter city name")
            Country=input("enter Country name")
            myPhoneBook[name]=[ph,email,city,Country]#adding it to the dict
            print("contact added successfully")
            add_contact(conn,(name,ph,email,city,Country)) # adding it to the database
            
            
            
    elif(choice ==2):
        print("CONTACT DETAILS")
        for name,details in myPhoneBook.items():
            print("Name = ",name.upper())
            print("Phone Number = ",details[0])
            print("Email - ID = ",details[1])
            print("City = ",details[2])
            print("state = ",details[3])
            print("===============================")
        

    elif(choice ==3):
        print("Search Contact")
        sName=input("Enter the name of the contact to be searched")
        if sName in myPhoneBook:
            print("Name = ",sName)
            print("phone Number = ",myPhoneBook[sName][0])
            print("Email-ID = ",myPhoneBook[sName][1])
            print("City = ",myPhoneBook[sName][2])
            print("state = ",myPhoneBook[sName][3])

        else:
            print("contact Not found in phone book")

    elif(choice ==4):
        print("Deleting a contact")
        dname=input("enter the name of the contact to delete")
        if dname in myPhoneBook:
            print("contact ",dname," is found")
            print("do u want to delete",dname,"(y/n)?")
            ch=input("")
            if(ch == "y"):           
                del myPhoneBook[dname]
                delFromTable(conn,dname)
                print("contact deleted")
            else:
                print("not deleted")
        else:
            print("contact not found")
            
    elif(choice ==5):
        print("Editing a Contact")
        eName=input("enter name of the contact to be edited")
        if eName in myPhoneBook:
            print("contact found")
            print("current phone number = ",myPhoneBook[eName][0])
            ch=input("do u want to change(y/n)?")
            if(ch == 'y'):
                p=int(input("enter new phone number"))
                myPhoneBook[eName][0]=p
                print("phone number updated")
            else:
                print("phone number not changed")

            print("current Email -ID = ",myPhoneBook[eName][1])
            ch=input("do u want to change(y/n)?")
            if(ch == 'y'):
                e=input("enter new Email-ID")
                myPhoneBook[eName][1]=e
                print("Email-ID updated")
            else:
                print("Email-ID not changed")

            print("current City = ",myPhoneBook[eName][2])
            ch=input("do u want to change(y/n)?")
            if(ch == 'y'):
                c=input("enter new city")
                myPhoneBook[eName][2]=c
                print("City updated")
            else:
                print("city not changed")    

        else:
            print(eName ," contact not found for editing")
        
    elif(choice ==0):
        print("exiting phonebook management application")
        break
    else:
        print("wrong choice, Please check the menu")

print("END")
