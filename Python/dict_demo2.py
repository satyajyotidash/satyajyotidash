ph={"Roger":[98989898,"Roger@gmail.com","London","UK"],
    "Rahul":[898989898,"Rahul@hotmail.com","Banglore","India"],
    "Sachin":[99778866,"Sachin@ymail.com","Mumbai","India"],
    "Rohith":[767676766,"Rohith@live.com","Texas","USA"],
    "Anil":[987654321,"Anil@ymail.com","Munich","Germany"],
    "Police":(100,"police.help@gov.in","New Delhi","India")}

#ph["Sachin"][0]=999999999
#ph['Rahul'][1]='Rahul.D@yahoo.com'
#ph["Police"][0]=101
#print(ph.items())#[("Roger",[9898989898,"Roger@gmail.com","London,"UK"]),("Rahul",[898989898,"Rahul@hotmail.com",]),(),(),(),()]


for name,details in sorted( ph.items()):
    print("Name = ",name)
    print("Phone = ",details[0])
    print("Email-ID = ",details[1])
    print("City = ",details[2])
    print("Country = ",details[3])
    print("**********************************")
