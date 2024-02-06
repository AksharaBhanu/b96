import openpyxl

#open the excel file (work book)
wb=openpyxl.open("../data/Book1.xlsx")
#goto sheet1
sheet=wb['Sheet2']
for i in range(1,4):
    for j in range(1,4):
        #get the value present in the cell
        v=sheet.cell(i,j).value
        print(v,end=' ')
    print()
#close the excel file
wb.close()