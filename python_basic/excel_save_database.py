# -*- coding: utf-8 -*-
import pyexcel as pe
import pyexcel.ext.xls # import it to handle xls file
import pyexcel.ext.xlsx # import it to handle xlsx file
import json
import pyexcel
import sqlite3 as lite
from openpyxl import Workbook
from openpyxl import load_workbook
import datetime, time
import os
from nt import chdir
import shutil
"""
sheets = book.to_dict()

for namename in sheets.keys():
    print(namename)
    getsheet = pyexcel.get_sheet(file_name="test.xlsx", name=namename)
    print getsheet.row[1]
#for name in sheet:
    #print name
"""
import os

newpath='C:\\temp_read_Excel\\'

if not os.path.exists(newpath): os.makedirs(newpath)


#directory_path = "\\\Ecs01\\pj_est\\2015-TWN\\31-14Q2289A 日勝生大橋頭國小聯開案機電工程\\02估價資料\\02廠商報價\\2015- 廠商報價"
#directory_path="C:\Python2.7.10\project_database\excel_database"
directory_path="V:\\09-Final Price Data Bank\\F-一般閥件(特殊閥)"
directory_path=unicode(directory_path,'utf8')
fileNum=0
for pathinfile, subdirs, files in os.walk(directory_path):
    for name in files:
        fileEXT = os.path.splitext(name)[1]
        fileNum+=1
        print fileNum , "exception"
        if (fileEXT == '.xls' or fileEXT== '.xlsx') and fileNum>=88:
            if fileEXT=='.xls':
                tempName='123.xls'
            if fileEXT=='.xlsx':
                tempName='123.xlsx'
            
            
            
            oldNamePath = os.path.join(pathinfile,name)
            
            
            srcfile = oldNamePath
            dstroot ='C:\\temp_read_Excel'
            
            
            

            
            shutil.copy(srcfile, dstroot)
            TempOldNamePath = os.path.join(dstroot,name)
            TempNewNamePath = os.path.join(dstroot,tempName)
            
            os.rename(TempOldNamePath,TempNewNamePath)
            
            
            #pathstring="C:\Python2.7.10\project_database\excel_database"
            pathstring='C:\temp_read_Excel'
            filepath_data=unicode(pathinfile)
            print filepath_data, "database path"
            FileNamestring=name
            print dstroot,tempName, "read"
            os.chdir(dstroot)
            print os.getcwd()
            while True:
                try:
                    book_dict = pyexcel.get_book_dict(file_name=tempName, path=dstroot)
                    break
                except ValueError:
                    os.remove(TempNewNamePath)
                    print "Oops!  That was no valid number.  Try again..."
            #book_dict = pyexcel.get_book_dict(file_name=tempName, path=dstroot)
            #isinstance(book_dict, OrderedDict)
            con = lite.connect('database.db')
            with con:
                cur=con.cursor()
                sheetnum=0
                for key, val in book_dict.items():
                    #sheetName_ID
                    sheetnum+=1
                    print(key)
                    sql_datacheck="SELECT * FROM excel_file WHERE PATH=? AND FileName=? AND File_SheetName=?"
                    sql_pathnamesheet="INSERT INTO excel_file(PATH,FileName,File_SheetName,File_Datetime) VALUES(?,?,?,?)"
                    now = datetime.datetime.now()
                    PathNameSheet_para=[filepath_data,FileNamestring,key,now]
                    fileCheck_Para=[filepath_data,FileNamestring,key]
                    for checker in con.execute(sql_datacheck, fileCheck_Para):
                        rownum=0
                        for valrow in val:
                            rownum+=1
                            colnum=0
                            for valcol in valrow:
                                colnum+=1
                                if valcol!='':
                                    sql_check="SELECT * FROM excel_content WHERE Sheet_Name=? and Row_Number=? and Col_Number =?"
                                    sql_update="UPDATE excel_content SET Cell_Data=? WHERE Sheet_Name=? and Row_Number=? and Col_Number =?"
                                    sql_insert="INSERT INTO excel_content(Sheet_Name,Row_Number,Col_Number,Cell_Data) VALUES(?,?,?,?)"
                                    content_check_para=[checker[0],rownum,colnum]
                                    insert_para=[checker[0],rownum,colnum,valcol]
                                    update_para=[valcol,checker[0],rownum,colnum]
                                    #cell exist
                                    for celldataval in con.execute(sql_check, content_check_para):
                                        con.execute(sql_update, update_para)
                                        
                                        break
                                    else:
                                    
                                        con.execute(sql_insert, insert_para)
                             
                        #os.remove(TempNewNamePath)
                        break
                    else:    
                        con.execute(sql_pathnamesheet, PathNameSheet_para)
                        for thisID in con.execute(sql_datacheck, fileCheck_Para):
                            
                            rownum=0
                        
                            for valrow in val:
                                rownum+=1
                                colnum=0
                                for valcol in valrow:
                                    colnum+=1
                                    if valcol!='':
                                        sql_check="SELECT * from excel_content"
                                        sql_insert="INSERT INTO excel_content(Sheet_Name,Row_Number,Col_Number,Cell_Data) VALUES(?,?,?,?)"
                                        insert_para=[thisID[0],rownum,colnum,valcol]
                                        con.execute(sql_insert, insert_para)
            
            os.remove(TempNewNamePath)
            


