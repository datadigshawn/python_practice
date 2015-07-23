# -*- coding: utf-8 -*-
#Open file dialog => Print all worksheets => Choose worksheet => Read Value
from openpyxl import load_workbook
from array import *
import Tkinter
import tkFileDialog
j=-1
arr=[]
#Open File Dialog
Tkinter.Tk().withdraw() 
filepath = tkFileDialog.askopenfilename()
print filepath

#Print All WorkSheet Name
wb=load_workbook(filename=filepath)
result= wb.get_sheet_names()
for i in result:
    j += 1
    arr.append([j,i])
    print "(", j, ")", i

#Choose the Worksheet
WS=int(raw_input("Enter WorkSheet Number:"))

WorkSheet = arr[WS][1]
print WorkSheet
#It doesn't matter if it is Chinese
#filepath=unicode(filepath,'utf8')
sheet_ranges = wb[WorkSheet]

#Read the values of  cells in worksheet
for i in range(1,5,1):
     Val=("A" + str(i))
     print(sheet_ranges[Val].value)
     Val2=("B" + str(i))
     print(sheet_ranges[Val2].value)
     values = (sheet_ranges[Val2].value)
     arr.append(values)
