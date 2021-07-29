import re

#data="zsf3q zfdf sachin_rt99@gmail.com asab55344 9845098450 abn Roger.K123@yahoo.co.in asa9886098860 abc sdfsd9885098850ab#"
f=open("C:\\Users\\dell\\Desktop\\Adv_python\\Adv_python\\Day3\\contacts.txt",mode="r")
data=f.read()
f.close()


res=re.findall("[\w.]+@[a-zA-Z.]+",data)#[('sachin_rt99','@','gmail.com'),('Roger.K123','@','yahoo.co.in')]
if(res):
    print("Match found")
    print(res)
    #print("Email :: ",res.group(0))
    #print("Username :: ",res.group(1))
    #print("Hostname :: ",res.group(2))
      
else:
    print("Match not found")


