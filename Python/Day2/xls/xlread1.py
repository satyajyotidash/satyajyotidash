import xlrd

wb=xlrd.open_workbook("C:\\Users\\dell\\Desktop\\DanskeIT\\myphonebook.xls")
print("number of sheets ",wb.nsheets)
for snum in range(0,wb.nsheets):
    

print("number of rows = ",sheet.nrows)
for row in range(0,sheet.nrows):
    data=sheet.row_values(row)
    print(data)
