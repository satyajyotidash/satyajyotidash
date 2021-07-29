def validate_IP(ip):
    print("validate_IP function from module3")
    if(ip.count(".") != 3):
        return False
    else:
        ipnums=ip.split(".")#['192','168','65','43']
        for num in ipnums:
            if(int(num) >= 255):
                return False

        return True


def sayHello():
    print("sayHello function from module3")
    print("in sayhello function")
    print("sayhello function running")
    print("sayhello function ends")
