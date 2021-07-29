
mydata=["england","germany","netharlands","spain","france","Italy"]

import xlrd 
from xlutils.copy import copy

while True:
    try:
        fname=input("enter file name")
        rwb = xlrd.open_workbook(fname)
        break
    except(FileNotFoundError) as err:
        print("file not present")
  
wwb = copy(rwb)

s = wwb.get_sheet(1)
count=0
for country in mydata:
    s.write(count,5,country)
    count=count+1

wwb.save(fname)


