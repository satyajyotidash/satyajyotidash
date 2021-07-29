#from mypackage.module1 import cube
#from mypackage.module2 import myMax
#from mypackage.module3 import validate_IP,sayHello
import mypackage.module3 as m3


res=m3.validate_IP('192.168.45.64')
print("res = ",res)

m3.sayHello()
