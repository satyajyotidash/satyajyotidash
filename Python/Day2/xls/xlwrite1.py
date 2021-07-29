import xlwt


wb=xlwt.Workbook()
sheet1=wb.add_sheet("c_sheet1")
sheet2=wb.add_sheet("c_sheet2")
sheet3=wb.add_sheet("c_sheet3")
sheet4=wb.add_sheet("c_sheet4")

sheet1.write(0,0,"sunday")
sheet1.write(0,1,"monday")
sheet1.write(0,2,"tuesday")
sheet1.write(0,3,"wednesday")
sheet1.write(0,4,"thursday")
sheet1.write(0,5,"friday")
sheet1.write(0,6,"satuarday")

sheet4.write(0,0,"sunday")
sheet4.write(1,0,"monday")
sheet4.write(2,0,"tuesday")
sheet4.write(3,0,"wednesday")
sheet4.write(4,0,"thursday")
sheet4.write(5,0,"friday")
sheet4.write(6,0,"satuarday")

wb.save("C:\\Users\\dell\\Desktop\\DanskeIT\\data.xls")
