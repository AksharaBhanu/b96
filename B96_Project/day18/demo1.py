import openpyxl

#open the excel file (work book)
wb=openpyxl.open("f:/Book1.xlsx")
#goto sheet1
sheet=wb['Sheet1']
#get the value present in the cell
v=sheet.cell(1,1).value
print(v)
#close the excel file
wb.close()

