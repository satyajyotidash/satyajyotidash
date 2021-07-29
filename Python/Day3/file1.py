print("File Handling Demo")

f1=open("myfile.txt",mode='w')
f2=open("testfile.txt",mode='w')

while(True):
    data=input("Enter a string and quit to stop")
    if(data == "quit"):
        break
    else:
        f1.write(data+"\n")
        f2.write(data.upper()+"\n")


f1.close()
f2.close()
