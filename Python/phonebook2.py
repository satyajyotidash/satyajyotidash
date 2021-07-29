print("Phone Book Contact Management Application")
ph={"Roger":[98989898,"Roger@gmail.com","London","UK"],
    "Rahul":[898989898,"Rahul@hotmail.com","Banglore","India"],
    "Sachin":[99778866,"Sachin@ymail.com","Mumbai","India"],
    "Rohith":[767676766,"Rohith@live.com","Texas","USA"],
    "Anil":[987654321,"Anil@ymail.com","Munich","Germany"],
    "Police":(100,"police.help@gov.in","New Delhi","India")}

while(True):
    print("1 : Add Contact")
    print("2 : Search Contact")
    print("3 : Display all Contact")
    print("4 : Delete Contact")
    print("5 : Edit Contact")
    print("0 : Exit")
    choice=int(input("Enter your choice :: "))#3
    if(choice == 1):
        print("Addding Contact")
        name=input("Enter name of the contact to add :: ")
        if (name in ph):
            print("Contact exist with name ",name)
            print("Duplicate contact can't be added")
        else:
            print("Contact doesn't exist with name ",name)
            print("Please enter other details for ",name)
            phone=int(input("Enter Phone number :: "))
            email=input("Enter Email ID :: ")
            city=input("Enter City Name :: ")
            country=input("Enter Country name :: ")
            ph[name]=[phone,email,city,country]
            print("Contact added successfully ")
    elif(choice == 2):
        print("Searhcing Contact")
        sname=input("Enter name of the contact to search :: ")
        if sname in ph:
            print("Contact found ")
            print("Name = ",sname)
            print("Phone = ",ph[sname][0])
            print("Email = ",ph[sname][1])
            print("City = ",ph[sname][2])
            print("Country = ",ph[sname][3])

        else:
            print(sname," contact not found in phone book")
    elif(choice == 3):
        print("Dispalying Contacts")
        for n,d in sorted(ph.items()):
            print("Name = ",n)
            print("Phone = ",d[0])
            print("Email = ",d[1])
            print("City = ",d[2])
            print("Country = ",d[3])
            print("***************************")
    elif(choice == 4):
        print("Delete Contact")
        dname=input("Enter name of the contact to delete :: ")
        if(dname in ph):
            print("Contact found")
            ch=input("Do you want to delete(y/n)?")
            if(ch == 'y'):
                del ph[dname]
                print(dname," contact deleted successfully")
            else:
                print("contact not deleted")

        else:
            print(dname," contact not found in phone book")
    elif(choice == 5):
        print("Edit Contact")
        print("Edit Contact logic will be implemented")
    elif(choice == 0):
        print("Exiting Phone Book Contact Management Application")
        break
    else:
        print("Wrong choice ")
        print("Please check the menu and enter accordingly")
        


print("GoodBye!!!")
