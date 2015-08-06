# -*- coding: utf-8 -*-
from Tkinter import *
import scraping
from bs4 import BeautifulSoup
import requests
import array
root = Tk()
root.geometry('500x500+500+300')
#Frame
F1 = Frame(root)
F1.grid(row=0, column=0)
F2 = Frame(root)
F2.grid(row=0, column=1)
#Label Change In Frame
#LMenu= Label(F1, text = '0')
#LMenu.grid(row=0, column=0)

def hello():
    #L1=Label(root, font = "Helvetica 12", text="hi")
    #L1.pack()
    LMenu['text'] = str(int(LMenu['text']) + 1)
    
    return
def ciao():
    L1=Label(root, font = "Helvetica 12", text="ciao")
    L1.pack()
    return
def AL():
    website = "http://www.taiwancable.org.tw/Metal.aspx?Al"
    TableName = "ctl00_ContentPlaceHolder1_priceGridView"
    ScrapFrame(website, TableName)
    for child in F1.winfo_children():
       child.destroy()
    LMenu= Label(F1, text = '鋁')
    LMenu.grid(row=0, column=0)
    return
def Copper():
    website = "http://www.taiwancable.org.tw/Metal.aspx?Co"
    TableName = "ctl00_ContentPlaceHolder1_priceGridView"
    ScrapFrame(website, TableName)
    for child in F1.winfo_children():
       child.destroy()
    LMenu= Label(F1, text = '銅')
    LMenu.grid(row=0, column=0)
def Nickel():
    website = "http://www.taiwancable.org.tw/Metal.aspx?Ni"
    TableName = "ctl00_ContentPlaceHolder1_priceGridView"
    ScrapFrame(website, TableName)
    for child in F1.winfo_children():
       child.destroy()
    LMenu= Label(F1, text = '鎳')
    LMenu.grid(row=0, column=0)
    return
def Lead():
    website = "http://www.taiwancable.org.tw/Metal.aspx?Le"
    TableName = "ctl00_ContentPlaceHolder1_priceGridView"
    ScrapFrame(website, TableName)
    for child in F1.winfo_children():
       child.destroy()
    LMenu= Label(F1, text = '鉛')
    LMenu.grid(row=0, column=0)
    return
def Tin():
    website = "http://www.taiwancable.org.tw/Metal.aspx?Zi"
    TableName = "ctl00_ContentPlaceHolder1_priceGridView"
    ScrapFrame(website, TableName)
    for child in F1.winfo_children():
       child.destroy()
    LMenu= Label(F1, text = '錫')
    LMenu.grid(row=0, column=0)
    return
#網路數據
def AllPrice():
    count = 0 
    #Clean F1, F2 Frame
    for child in F1.winfo_children():
       child.destroy()
    for child in F2.winfo_children():
       child.destroy()
    
    #exe all function
    OilPrice = scraping.ScrapingOil()
    OilPrice.WTexasOil()
    LMEPrice = scraping.ScrapingLME()
    LMEPrice.LMEselect()
    CPrice = scraping.ScrapingCurrency()
    CPrice.CurrencySelect()
    #print CPrice.CResultArr
    
    def EntryIn(row, col, text):

        InputE = StringVar()
        EOil = Entry(F1, width=10, font = "Helvetica 8",  textvariable=InputE, state='readonly', borderwidth=0)   
        EOil.grid(row=row, column=col)
        InputE.set(text)
    
    # West Texas Oil
    EntryIn(0,0,"西德州原油")
    for i, d in OilPrice.DateArr:
        EntryIn(1,i,d)
    for j, p in OilPrice.PriceArr:
        EntryIn(2,j,p)
    #LME
    EntryIn(3,0,"LME")
    
    EntryIn(4, 1, "銅")
    EntryIn(4, 2, "鋁")
    EntryIn(4, 3, "鎳")
    EntryIn(4, 4, "鋅")
        
    for LMEVal in LMEPrice.priceSelect:
        count += 1
        EntryIn(5, count, LMEVal)
    #Currency
    EntryIn(7,0,"USD")
    EntryIn(8,0,CPrice.CResultArr[0])
    EntryIn(7,1,"JPY")
    EntryIn(8,1,CPrice.CResultArr[1])
    EntryIn(7,2,"EUR")
    EntryIn(8,2,CPrice.CResultArr[2])
    EntryIn(7,3,"CNY")
    EntryIn(8,3,CPrice.CResultArr[3])
    return
def ScrapFrame(website, TableName):
    for child in F2.winfo_children():
       child.destroy()
    REL1 = scraping.ScrapingInfo(website, TableName)
    #REL1 = scraping.ScrapingInfo("http://www.taiwancable.org.tw/Metal.aspx?Al","ctl00_ContentPlaceHolder1_priceGridView")
    REL1.GetHTMLCode()
    REL1.ParserTarget()
    #print REL1.dataArr2GUI
    #header
    thead = ["日期", "匯率", "現貨\n最低", "現貨\n最高", "收盤價\n最低", "收盤價\n最高", "三個月\n期貨現貨\n最低", "三個月\n期貨現貨\n最高", "三個月\n期貨收盤價\n最低", "三個月\n期貨收盤價\n最高"]
    i = 0
    for Name in thead:
       i += 1
       EH = Label(F2, font = "Helvetica 12", text=Name)
       EH.grid(row=0, column=i)
    def EntryInput(rowNum, colNum, text):
            textInput = StringVar()
        
            if colNum == 1:
                widthSet = 10
            else:
                widthSet = 6
       
            #data
            E1 = Entry(F2, width=widthSet, font = "Helvetica 12 bold",  textvariable=textInput, state='readonly', borderwidth=0)
            E1.grid(row=rowNum, column=colNum)
            textInput.set(text)
    for name in REL1.dataArr2GUI:
            if name[1] == 10 and name[2].isdigit() == False:
                continue
               
            else:
                
                EntryInput(name[0],name[1],name[2])
    return
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
editmenu.add_command(label="鋁", command=AL)
editmenu.add_command(label="銅", command=Copper)
editmenu.add_command(label="鎳", command=Nickel)
editmenu.add_command(label="錫", command=Tin)
editmenu.add_command(label="鉛", command=Lead)
menubar.add_cascade(label="台灣電線電纜金屬價格", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="顯示數據", command=AllPrice)

helpmenu.add_command(label="Export Excel", command=hello)
menubar.add_cascade(label="網路數據", menu=helpmenu)

# display the menu
root.config(menu=menubar)
mainloop()
