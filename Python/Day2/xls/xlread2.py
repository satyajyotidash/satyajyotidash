import xlrd

wb=xlrd.open_workbook("myphonebook.xls")
sheet=wb.sheet_by_index(0)
for col in range(0,sheet.ncols):
    data=sheet.col_values(col)
    print(data)


