import openpyxl

wb=openpyxl.open('../data/Book1.xlsx')
allsheets=wb.sheetnames
count=len(allsheets)
print(allsheets)
wb.close()
