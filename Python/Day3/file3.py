print("File Handling Demo")

f1=open("testfile.txt",mode='r')

for line in f1:
    line=line.rstrip()
    data=line.split(" ")
    print(data)
    
f1.close()
