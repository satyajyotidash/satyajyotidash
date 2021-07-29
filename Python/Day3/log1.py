from time import sleep,ctime
f=open("logfile.txt",mode="w")

f.write(str(ctime())+" :: Package loaded "+"\n")
sleep(5)
f.write(str(ctime())+" :: Data base connected loaded "+"\n")
sleep(3)
f.write(str(ctime())+" :: Client1 request recieved "+"\n")
sleep(7)
f.write(str(ctime())+" :: Client served and request closed "+"\n")
f.close()
