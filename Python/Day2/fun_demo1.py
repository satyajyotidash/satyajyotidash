print("functions demo")

def myMax(a,b):
   
    if(a>b):
       return a
    elif(a == b):
        return "both are same"
    else:
        return b


print("in main script")
print("before myMax is called")
res=myMax(65,65)
print("res = ",res)
print("type of res = ",type(res))
print("after myMax is called")
