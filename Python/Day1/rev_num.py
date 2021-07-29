print("reverse number demo")
num=int(input("Enter a number :: "))#8769

rev=0

while(num):
    rem=num%10#rem=8%10 =8
    rev=rev*10+rem #rev=967*10+8 =9678
    num=num//10#num=8//10=0


print("reverse number = ",rev)
