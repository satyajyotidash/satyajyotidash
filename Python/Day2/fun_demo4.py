print("default and keyword argument demo")

def mySimpleIntrest(P=25000,Y=1,R=10):
    print("P = ",P)
    print("Y = ",Y)
    print("R = ",R)
    total = P + P*Y*R/100
    return total



print("in main script")
amt=mySimpleIntrest(R=9,P=20000,Y=5)#keyword argument passing
print("Total amount = ",amt)
print("bye")
