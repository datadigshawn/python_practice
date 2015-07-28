"""# -*- coding: utf-8 -*-
#coding==utf-8 """

from Tkinter import *
import os
import re
import sets
import json
from array import *
#List the First Stage Folder Name
def FirstBox():
    PathArr=[]
    filepath = "V:\\09-Final Price Data Bank"
    filepath=unicode(filepath,'utf8')
    print filepath
    dirs = os.listdir( filepath )
    for file in dirs:
        matchObj = re.match("(^[A-Z]{1}[-])", file)
        if matchObj:
            
            secondPath = ("%s\\%s" % (filepath, file))
            print type(file)
            PathArr.append(file)
    
    return PathArr
            
#Click First List n Generate Second List
def onSelect(val):
        SListValue=[]
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        SList.delete(0, END)
        #Read Second List Value
        filepath = "V:\\09-Final Price Data Bank"
        #filepath=unicode(filepath,'utf8')
        secondPath = ("%s\\%s" % (filepath, value))
        print secondPath
        

        os.chdir(secondPath)
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                matchObj = re.match("(^[A-Z]{1}[0-9]{2}[-])", name)
                if matchObj:
                    #text1=name.decode("BIG5")
                    JsonUno = name[0:1]
                    JsonDue = name[0:3]
                    #First Three Word Combine with JSON
                    with open('C:\\Python27\\project_database\\data-utf8.json', 'r') as f:
                         data = json.load(f)
                    SecondName = data[JsonUno][JsonDue]
                    Sname = ("%s %s" % (name[0:3], SecondName))
                    #END of Json
                    SListValue.append(Sname)
        Unique = sets.Set(SListValue)
        Unique = sorted(Unique)
        for Sval in Unique:
            SList.insert(END, Sval)
        
        var.set(secondPath)
        
        
def GetPath(val):
    anchor = val.widget
    index = anchor.curselection()
    value = anchor.get(index)
    TList.delete(0,END)
    #Find Fist Stage Path
    filepath = "V:\\09-Final Price Data Bank"
    filepath=unicode(filepath,'utf8')
    print filepath
    dirs = os.listdir( filepath )
    for file in dirs:
        matchObj = re.match("(^[A-Z]{1}[-])", file)
        if matchObj:
            find = str(file[0:1])
            befind = str(value[0:1])
            #Generate Second Stage Path
            if find == befind:
                FilterPath = ("%s\\%s" % (filepath, file))
                os.chdir(FilterPath)
                for root, dirs, files in os.walk(".", topdown=False):
                    for targets in files:
                        if targets[0:3] == value[0:3]:
                            print targets
                            target=targets.decode("BIG5")
                            TList.insert(END, target)
    print value

    var.set(value)
    return
#Open the External File
def openfile(val):
    #Get the Third Stage Value
    anchor = val.widget
    index = anchor.curselection()
    value = anchor.get(index)
    #First Stage Path
    filepath = "V:\\09-Final Price Data Bank"
    filepath=unicode(filepath,'utf8')
    dirs = os.listdir( filepath )
    for file in dirs:
        matchObj = re.match("(^[A-Z]{1}[-])", file)
        if matchObj:
            find = str(file[0:1])
            befind = str(value[0:1])
            #Generate Second Stage Path
            if find == befind:
                FilterPath = ("%s\\%s" % (filepath, file))
                os.chdir(FilterPath)
                for root, dirs, files in os.walk(".", topdown=False):
                    for targets in files:
                        OpenPath = ("%s\\%s" % (FilterPath, value))

    os.startfile(OpenPath)
                        
                        
    
root = Tk()

var = StringVar()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
scrollbar2 = Scrollbar(root)
scrollbar2.pack( side = RIGHT, fill=Y )
#First List
FirstList = Listbox(root, yscrollcommand = scrollbar.set, width=60, height=12 )
First=FirstBox()
for line in First:
   FirstList.insert(END, line)
FirstList.pack()
FirstList.bind("<<ListboxSelect>>", onSelect)

scrollbar.config( command = FirstList.yview )

#Second List
SList = Listbox(root, yscrollcommand = scrollbar2.set, width=60, height=12 )

    
SList.pack()
SList.bind("<<ListboxSelect>>", GetPath)
scrollbar2.config( command = SList.yview )

#Third List
TList = Listbox(root, yscrollcommand = scrollbar2.set, width=60, height=12 )

    
TList.pack()
TList.bind("<<ListboxSelect>>", openfile)


SelectedVal=Label(root, text=0, textvariable=var).pack()

mainloop()
