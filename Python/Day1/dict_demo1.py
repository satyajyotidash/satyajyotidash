ph={"Roger":98989898,"Rahul":898989898,"Sachin":99778866,
    "Rohith":767676766,"Anil":987654321}


print(ph)
#print(type(ph))
#print(len(ph))
#print("after update")
#ph['Sourav']=9845098450
#print(ph)
#print(ph.keys())#[, , , , ]
#print(ph.values())#[, , , , ]
#print(ph.items())#[("Roger",98989898),("Rahul",898989898),(),(),()]


for name,phone in ph.items():
    print("Name = ",name)
    print("Phone = ",phone)
    print("**************************")

dname=input("Enter name of the contact to delete :: ")
if dname in ph:
    print("Contact found ")
    ch=input("Do you want delete(y/n)?")
    if(ch == 'y'):
        del ph[dname]
        print(dname," contact deleted")
else:
    print("Contact not found")


print("after Delete")

for name,phone in ph.items():
    print("Name = ",name)
    print("Phone = ",phone)
    print("**************************")


    
