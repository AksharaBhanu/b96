import openpyxl

#open the excel file
wb=openpyxl.open('../data/book1.xlsx')
sheet=wb['Sheet2']

rc=sheet.max_row  #count the number of rows
print(rc)

cc=sheet.max_column  #count the number of columns
print(cc)

wb.close()
