print("Exception Handling Demo")
myList=[11,22,33,44,55]

while(True):
    num=int(input("Enter Numerator :: "))#88
    den=int(input("Enter Denominatore :: "))#11
    try:
        res=num//den
        print("res = ",res)
        print("myList[",res,"] = ",myList[res])
        num=input("Enter a number :: ")#65
        num=int(num)
        print("num = ",num)
    except(ZeroDivisionError) as err:
        print("Exception raised and handled")
        print("Zero dividion error")
        print(err)
    except(IndexError) as err:
        print("Exception raised and handled")
        print("Index error")
        print(err)
    except(ValueError) as err:
        print("Exception raised and handled")
        print("Value error")
        print(err)
    choice=input("Do you want to continue(y/n)?")
    if(choice == 'n'):
        break

print("End")
print("Bye!!!")
    
