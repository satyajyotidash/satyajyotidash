def myMax(a,b):
    '''
    >>> myMax(25,75)
    75
    >>> myMax(54,12)
    54
    >>> myMax(11,11)
    'both are same'
    >>> myMax(-10,-20)
    -10
    >>> myMax(0,-20)
    0
    >>> myMax(0,0)
    'both are same'
    >>> myMax(-20,-20)
    'both are same'
    '''
    if(a > b):
        return a
    elif(a==b):
        return "both are same"
    else:
        return b


def mul(a,b):
    '''
    >>> mul(10,5)
    50
    >>> mul(30,0)
    0
    >>> mul('d',5)
    'ddddd'
    >>> mul (-20,0)
    0
    >>> mul(-20,-5)
    100
    '''
    return a*b

def fact(num):
    '''
    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    >>> fact(4)
    24
    >>> fact(5)
    120
    '''
    if(num==0):
        return 1
    else:
        return num * fact(num-1)

def validate_IP(ip):
    '''
    >>> validate_IP('192.168.5.43')
    True
    >>> validate_IP('192.168.56.4.97.8')
    False
    >>> validate_IP('192.168.345.43')
    False
    >>> validate_IP('192.168')
    False
    >>> validate_IP('192.168.255.43')
    True
    >>> validate_IP('255.255.255.255')
    True
    >>> validate_IP('192.168.254.43')
    True
    '''
    if(ip.count(".") != 3):
        return False
    else:
        ipnums=ip.split(".")#['192','168','65','43']
        for num in ipnums:
            if(int(num) >= 255):
                return False

        return True
