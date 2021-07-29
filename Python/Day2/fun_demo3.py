print("IP Validation")

def validate_IP(ip):
    if(ip.count(".") != 3):
        return False
    else:
        ipnums=ip.split(".")#['192','168','65','43']
        for num in ipnums:
            if(int(num) > 255):
                return False

        return True
        




print("in Main script")
ip=input("Enter a IP address to validate :: ")#192.168.65.43
res=validate_IP(ip)
if(res == True):
    print("Valid IP Address")
else:
    print("Invalid IP Adrress")
