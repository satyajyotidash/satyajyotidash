import time


cnt=0

while(cnt<100):
    print("in while loop")
    print("cnt = ",cnt)
    print("current time =",time.ctime())
    time.sleep(1)
    cnt=cnt+1

print("bye")
