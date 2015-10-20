# -*- coding: utf-8 -*-
from xlwings import Workbook, Sheet, Range, Chart
import win32com.client

xl = win32com.client.Dispatch("Excel.Application")
xl.Visible = False
wb = xl.Workbooks.Open(r'C:\Python2.7.10\project_database\xlwings\AddComment.xlsx')

sheet = wb.ActiveSheet
sheet.Range("A1").AddComment()
sheet.Range("A1").Comment.Visible = True
commentString ='檔 不能沒有註解'
commentString=(commentString).decode('utf-8')    
sheet.Range("A1").Comment.Text(commentString)
wb.SaveAs(r'C:\Python2.7.10\project_database\xlwings\AddComment.xlsx')
xl.DisplayAlerts = False
wb.Close(True)
xl.Quit()
