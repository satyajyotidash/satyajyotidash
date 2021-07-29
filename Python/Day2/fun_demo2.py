print("functions demo")

def myOperations(a,b):
    x1=a+b
    x2=a-b
    x3=a*b
    x4=a/b
    x5=a//b
    x6=a%b
    x7=a**b
    return x1,x2,x3,x4,x5,x6,x7
   
    


print("in main script")
print("before myMax is called")
r1,r2,r3,r4,r5,r6,r7=myOperations(20,3)
print("r1 = ",r1)
print("r2 = ",r3)
print("r3 = ",r3)
print("r4 = ",r4)
print("r5 = ",r5)
print("r6 = ",r6)
print("r7 = ",r7)

