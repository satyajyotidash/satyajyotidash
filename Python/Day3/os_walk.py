import os
from time import sleep
print("os.walk demo")


for root,dirs,files in os.walk("C:\\Users\\dell\\Desktop\\DanskeIT"):
    print(root)
    for d in dirs:
        print(os.path.join(root,d))
    for f in files:
        pth=os.path.join(root,f)
        print(pth)
        if(os.path.getsize(pth) == 0):
            print(pth," file size is 0")
            ch=input("Do you want to delete(y/n)?")
            if(ch == 'y'):
                os.unlink(pth)
                print(pth," file deleted")
