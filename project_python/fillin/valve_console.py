# -*- coding: utf-8 -*-
from Tkinter import *
from bs4 import BeautifulSoup
import requests
import array
import sqlite3 as lite
import sys
import pyperclip
import textConvertor
root = Tk()
root.geometry('850x300+500+300')
#Frame
F1 = Frame(root)
F1.grid(row=0, column=0)
F2 = Frame(root)
F2.grid(row=0, column=1)
F3 = Frame(root)
F3.grid(row=1, column=1)

def Filter_Valve():
    GETArr=[]
    
    
    #refresh Frame F2
    for child in F2.winfo_children():
       child.destroy()
    #def Entry
    def EntryIn(row, col, text):

        InputE = StringVar()
        EOil = Entry(F2, width=10, font = "Helvetica 8",  textvariable=InputE, state='readonly', borderwidth=0)   
        EOil.grid(row=row, column=col)
        InputE.set(text)
    def EntryInF3(row, col, text):

        InputE = StringVar()
        EOil = Entry(F3, width=10, font = "Helvetica 8",  textvariable=InputE, state='readonly', borderwidth=0)   
        EOil.grid(row=row, column=col)
        InputE.set(text)
    row_name=['Code','Size','Weight','Price','YFilter','Sieve','Connector','Sub1','Sub2','BRAND','Firm']
    #print Name on it
    for name in row_name:
        col  = row_name.index(name)
        EntryIn(1,col,name)
    #drop down list
    #Size
    def DropDown(r,c,cate):
        options=[]
        #select distinct
        con = lite.connect('test.db')
        with con:
            cur=con.cursor()
            sql_action=('SELECT DISTINCT %s FROM com_release_valve'% (cate))
            optionSQL = con.execute(sql_action)
            for op in optionSQL:
                options.append(op)
        variableW = StringVar(F2)
        variableW.set(options[0]) # default value
        WeightS = apply(OptionMenu, (F2, variableW) + tuple(options))
        WeightS.grid(row=r, column=c)
        return WeightS
    def get():
        for child in F3.winfo_children():
            child.destroy()
        rel=[]
        excelcopier=[]
        excelpaster=[]
        #copy size from excel
        c=pyperclip.paste()
        Input = textConvertor.Vavle_Text()
        excelcopier = Input.Action(c)
        """
        c=str(pyperclip.paste())
        clipGet=c.rstrip().split('\r\n')
        for cal in clipGet:
            excelcopier.append(int(cal))
        """
        for i in range(0,10):
            rel.append(GETArr[i].cget("text"))
        print rel


        """
        loop for every excel value
        """
        for coSize in excelcopier:
            #got select condition
            
            
            rel[1]=coSize  #replace size to the excel value
            FilterSelect=[]
            FilterIndex=[]
            rowNameIndex=(-1)
            #except none
            for result in rel:
                rowNameIndex += 1 #row name index
                if result != 'None':
                    FilterSelect.append(result)  #filter conditon   
                    FilterIndex.append(row_name[rowNameIndex])  #sql row name
                    
            print FilterSelect, FilterIndex
           
            # conbine the select condition
            ConditionShead = '=? AND '.join(map(str,FilterIndex))
            ConditionS = ('%s=?'%(ConditionShead))
            
            print ConditionS
            Scon = lite.connect('test.db')
            with Scon:
                cur=Scon.cursor()
                Size_action = ('SELECT Size From com_release_valve WHERE Size=?')
                Size_para = [coSize]
                filter_action=('SELECT * FROM com_release_valve WHERE %s'% (ConditionS))
                filter_para = FilterSelect
                #check if size exists
                for checkSize in con.execute(filter_action,filter_para):
                    
                
                    optionSQL = con.execute(filter_action,filter_para)
                    printFrow=5
                    for Fresult in optionSQL:
                        printFrow += 1
                        for Fcol in Fresult:
                            print Fcol, Fresult.index(Fcol)
                            EntryInF3(printFrow,Fresult.index(Fcol),Fcol)
                    excelpaster.append(Fresult[4])
                    break
                else:
                    excelpaster.append(0)
        #paste result to clipbroad
        PasteStr = '\n'.join(map(str,excelpaster))
        pyperclip.copy(PasteStr)
        pyperclip.paste()
    #list All dropdown list
    for name in row_name:
        ddcol= row_name.index(name)
        
        GETArr.append(DropDown(2,ddcol,name))

    #submit button
    But1 = Button(F2, command = get, text="enter")
    But1.grid(row = 3, column = 1)
    #sql select for print tilte
    con = lite.connect('test.db')
    with con:
        cur=con.cursor()
        sql_action='SELECT * FROM com_release_valuev'
menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="AutoFill", command=Filter_Valve)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Valve", menu=filemenu)



# display the menu
root.config(menu=menubar)
root.iconbitmap(r'C:\Python2.7.10\project_database\query\com_release_value\autofill.ico')
mainloop()
