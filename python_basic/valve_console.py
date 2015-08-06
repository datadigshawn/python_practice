# -*- coding: utf-8 -*-
from Tkinter import *
from bs4 import BeautifulSoup
import requests
import array
import sqlite3 as lite
import sys

root = Tk()
root.geometry('500x500+500+300')
#Frame
F1 = Frame(root)
F1.grid(row=0, column=0)
F2 = Frame(root)
F2.grid(row=0, column=1)


def hello():
    #L1=Label(root, font = "Helvetica 12", text="hi")
    #L1.pack()
    LMenu['text'] = str(int(LMenu['text']) + 1)
    
    return
def ciao():
    L1=Label(root, font = "Helvetica 12", text="ciao")
    L1.pack()
    return
#ADD in DATABASE
def Add_New():
    def EntryIn(row, col, text):

        InputE = StringVar()
        EOil = Entry(F2, width=10, font = "Helvetica 8",  textvariable=InputE, state='readonly', borderwidth=0)   
        EOil.grid(row=row, column=col)
        InputE.set(text)
    ETitle = []
    #Got the Value
    def get():
        #global YFilter
        INV1 = inputSql.get()
        INV2 = inputSql2.get()
        INV3 = inputSql3.get()
        print YFilterS.cget("text")
        print WeightS.cget("text")
        print SeiveS.cget("text")
        print S1S.cget("text")
        print S2S.cget("text")
        print BrandS.cget("text")
        Icon = lite.connect('test.db')
        with Icon:
            Icur=Icon.cursor()
            #Icur.execute("insert into com_release_valve(Code,Size,Price) values (?,?,?)",(INV1, INV2, INV3))
            
    #clear F2 frame
    for child in F2.winfo_children():
        child.destroy()
    #select title from database
    con = lite.connect('test.db')
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM com_release_valve")
        col_names = [cn[0] for cn in cur.description]
        nameCount =0
        for name in col_names:
            nameCount += 1
            print nameCount
            if nameCount >= 2 and nameCount<=10 :
                print name
                ETitle.append(name)
    #Title
    ETcol = 0
    for Entrytitle in ETitle:
        ETcol += 1
        EntryIn(0, ETcol, Entrytitle)
    #input entry
    inputSql = Entry(F2, width = 10)
    inputSql.grid(row = 1, column = 1)
    inputSql2 = Entry(F2, width = 10)
    inputSql2.grid(row = 1, column = 2)
    inputSql3 = Entry(F2, width = 10)
    inputSql3.grid(row = 1, column = 4)
    #input select
    #Table Drop Down List
    OPTIONS = ["NONE","YES","NO"]
    WOptions = ["組"]
    S1Options = ["一般型", "一字型"]
    S2Options = ["ST閘閥", "ST球閥"]
    BOptions = ["RS"]

    #weight
    variableW = StringVar(F2)
    variableW.set(WOptions[0]) # default value
    WeightS = apply(OptionMenu, (F2, variableW) + tuple(WOptions))
    WeightS.grid(row=1, column=3)
    #Y filter
    variableY = StringVar(F2)
    variableY.set(OPTIONS[0]) # default value
    YFilterS = apply(OptionMenu, (F2, variableY) + tuple(OPTIONS))
    YFilterS.grid(row=1, column=5)
    #Seives
    variableSeive = StringVar(F2)
    variableSeive.set(OPTIONS[0]) # default value
    SeiveS = apply(OptionMenu, (F2, variableSeive) + tuple(OPTIONS))
    SeiveS.grid(row=1, column=6)
    #Subject 1
    variableS1 = StringVar(F2)
    variableS1.set(S1Options[0]) # default value
    S1S = apply(OptionMenu, (F2, variableS1) + tuple(S1Options))
    S1S.grid(row=1, column=7)
    #Subject 2
    variableS2 = StringVar(F2)
    variableS2.set(S2Options[0]) # default value
    S2S = apply(OptionMenu, (F2, variableS2) + tuple(S2Options))
    S2S.grid(row=1, column=8)
    #Brand
    variableB = StringVar(F2)
    variableB.set(BOptions[0]) # default value
    BrandS = apply(OptionMenu, (F2, variableB) + tuple(BOptions))
    BrandS.grid(row=1, column=9)
    #submit button
    But1 = Button(F2, command = get, text="enter")
    But1.grid(row = 2, column = 1)
    
    
def value_db():
    #drop down list value print
    def EntryIn(row, col, text):

        InputE = StringVar()
        EOil = Entry(Table, width=10, font = "Helvetica 8",  textvariable=InputE, state='readonly', borderwidth=0)   
        EOil.grid(row=row, column=col)
        InputE.set(text)
    def option_changed(*args):
        Sel = format(variable.get())
        for child in Table.winfo_children():
            child.destroy()
        
        st = lite.connect('test.db')
        with st:
            stcur = st.cursor()
            stcur.execute('SELECT * FROM com_release_valve, Firm WHERE  Firm.Id = com_release_valve.Firm')
            col_names = [cn[0] for cn in stcur.description]
            rows = stcur.fetchall()
        ttcol = 0
        for ttitle in col_names:
            ttcol += 1
            
            EntryIn(1, ttcol, ttitle)
        rrow = 1
        for row in rows:
            rrow +=1
            rrcol = 0
            for name in row:
                rrcol +=1
                
                if rrcol <= 5:
                    print name, rrow, rrcol
                    EntryIn(rrow, rrcol, name)
    
        
    OPTIONS = []
    #clean F2 Flame
    for child in F2.winfo_children():
        child.destroy()
    #sqlite 
    con = lite.connect('test.db')
    with con:
        cur=con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        rows = cur.fetchall()
        for row in rows:
             row[0]
            
            
    #Table Drop Down List
    OPTIONS = ["ADD","LIST ALL"]
    variable = StringVar(F2)
    variable.set(OPTIONS[0]) # default value
    variable.trace("w", option_changed)
    w = apply(OptionMenu, (F2, variable) + tuple(OPTIONS))
    w.grid(row=1, column=1)
    Table = Frame(F2)
    Table.grid(row=2, column=1)
    
def GetValue():
    
    for child in F2.winfo_children():
       child.destroy()
    cut= Label(F2, text = "0")
    cut.grid(row=0, column=0)
    
menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=ciao)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="減壓閥", command=value_db)
editmenu.add_command(label="ADD", command=Add_New)
editmenu.add_command(label="鎳", command=hello)
editmenu.add_command(label="錫", command=hello)
editmenu.add_command(label="鉛", command=hello)
menubar.add_cascade(label="閥", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="顯示數據", command=hello)

helpmenu.add_command(label="Export Excel", command=hello)
menubar.add_cascade(label="網路數據", menu=helpmenu)

# display the menu
root.config(menu=menubar)
mainloop()
