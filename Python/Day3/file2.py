print("File Handling Demo")

f1=open("myfile.txt",mode='r')

for line in f1:
    line=line.rstrip()
    print(line)
    
f1.close()
