import openpyxl
wb = openpyxl.load_workbook(filename ='read-write-folder/files-to-read/beispiel1.xlsx')
sheet_ranges = wb['Tabelle1']
print(sheet_ranges['b1'].value)
print(sheet_ranges['b2'].value)
print(sheet_ranges['b3'].value)
print(sheet_ranges['b4'].value)