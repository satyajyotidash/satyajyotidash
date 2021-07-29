print("File Handling Demo")

with open("myfile.txt",mode='w') as f1:
    while(True):
        data=input("Enter a string and quit to stop")
        if(data == "quit"):
            break
        else:
            f1.write(data+"\n")


f1.write("sdfgjhknljbgjgjjyj")


