import openpyxl

wb=openpyxl.open('../data/Book1.xlsx')
sheet=wb['Sheet1']
sheet.cell(1,1).value='Python'
wb.save('../data/Book2.xlsx')
wb.close()