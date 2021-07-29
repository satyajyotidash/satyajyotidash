print("Exception Handling Demo")
myList=[11,22,33,44,55]

while(True):
    
    while(True):
        try:
            num=int(input("Enter Numerator :: "))#88
            break
        except(ValueError) as err:
            pass

    while(True):
        try:
            den=int(input("Enter Denominatore :: "))#11
            break
        except(ValueError) as err:
            pass
    try:
        res=num//den
        print("res = ",res)
        print("myList[",res,"] = ",myList[res])
        num=input("Enter a number :: ")#65
        num=int(num)
        print("num = ",num)
    except(ZeroDivisionError) as err:
        print("Exception raised and handled")
        print("divide by zero error")
        print(err)
    finally:
        print("in finally block")
        print("finally block always executes")
        print("finally block is used as clean up handlers")

    choice=input("Do you want to continue(y/n)?")
    if(choice == 'n'):
        break

print("End")
print("Bye!!!")
    
