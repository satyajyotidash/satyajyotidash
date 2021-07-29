print("variable number of arguments")

def adder(*args):
    s=0
    for val in args:
        s=s+val
    return s
    




print("in main script")
res=adder(1,2,3,4,5,6)
print("res = ",res)

res=adder(11,22)
print("res = ",res)

res=adder(11,22,33,44,55,66,77,88,99)
print("res = ",res)


res=adder(10,2,30,4,5,60,23,12,43,54,65,76,86,34,12,45,67,84)
print("res = ",res)


res=adder(10,20,30,40,50)
print("res = ",res)


