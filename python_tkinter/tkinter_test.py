"""
Listbox with scroll bar 
A Label will display what you have selected in Listbox
"""
from Tkinter import *
import os
#selected value on Listbox
def onSelect(val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)   
        var.set(value)
        
root = Tk()
var = StringVar()
#scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
#Listbox
mylist = Listbox(root, yscrollcommand = scrollbar.set, width=40, height=10 )
for line in range(20):
   mylist.insert(END, "No." + str(line))
mylist.pack()
mylist.bind("<<ListboxSelect>>", onSelect)

scrollbar.config( command = mylist.yview )
#Label which display what you've select
SelectedVal=Label(root, text=0, textvariable=var).pack()

mainloop()

"""
List all folder  in specified path

"""
# -*- coding: utf-8 -*-
import os 
filepath=""" Specified Path"""
filepath=unicode(filepath,'utf8')
dirs = os.listdir( filepath )        
for file in dirs:
   print file


"""
OPEN FILE By NAME
Triple List Box 
Select by category and Open File!!!!
"""
"""# -*- coding: utf-8 -*-
#coding==utf-8 """

from Tkinter import *
import os
import re
import sets
from array import *
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
            
def SecondBox():
    PathArr2=[]
    #Read Second List Value
    filepath = "V:\\09-Final Price Data Bank\\A-電器"
    filepath=unicode(filepath,'utf8')
    os.chdir(filepath)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            PathArr2.append(name)
    
    return PathArr2
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
                    
                    SListValue.append(name[0:3])
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
                        if targets[0:3] == value:
                            print targets
                            target=targets.decode("BIG5")
                            TList.insert(END, target)
    print value

    var.set(value)
    return

root = Tk()

var = StringVar()

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )
scrollbar2 = Scrollbar(root)
scrollbar2.pack( side = RIGHT, fill=Y )
#First List
FirstList = Listbox(root, yscrollcommand = scrollbar.set, width=40, height=10 )
First=FirstBox()
for line in First:
   FirstList.insert(END, line)
FirstList.pack()
FirstList.bind("<<ListboxSelect>>", onSelect)

scrollbar.config( command = FirstList.yview )

#Second List
SList = Listbox(root, yscrollcommand = scrollbar2.set, width=40, height=10 )

    
SList.pack()
SList.bind("<<ListboxSelect>>", GetPath)
scrollbar2.config( command = SList.yview )

#Third List
TList = Listbox(root, yscrollcommand = scrollbar2.set, width=40, height=10 )

    
TList.pack()
TList.bind("<<ListboxSelect>>", GetPath)


SelectedVal=Label(root, text=0, textvariable=var).pack()

mainloop()
