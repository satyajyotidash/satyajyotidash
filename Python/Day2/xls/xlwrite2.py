import xlwt

pb={"smith":[98989898,"smith@gmail.com","London","UK"],
    "jenny":[97658765,"jenny@ymail.com","washingtonDC","USA"],
    "will":[96669997,"will@hotmail.com","Paris","France"],
    "Rosy":[78899797,"rosy@yahoo.com","Munich","Germany"],
    "john":[98788788,"John@live.com","madrid","Spain"],
    "Roger":[9099988,"Roger@gmail.com","Sydney","Australia"],
    "kane":[677888,"kane@gmail.com","auckland","NewZealand"],
    "abe":[988888,"abe@gmail.com","Tokoyo","Japan"]}

wb=xlwt.Workbook()
sheet=wb.add_sheet("mycontacts")
sheet.write(0,0,"Name")
sheet.write(0,1,"Phone")
sheet.write(0,2,"Email")
sheet.write(0,3,"City")
sheet.write(0,4,"Country")
row=1
for name,details in pb.items():
    sheet.write(row,0,name)
    sheet.write(row,1,details[0])
    sheet.write(row,2,details[1])
    sheet.write(row,3,details[2])
    sheet.write(row,4,details[3])
    row=row+1

wb.save("C:\\Users\\dell\\Desktop\\DanskeIT\\myphonebook.xls")
    
    
