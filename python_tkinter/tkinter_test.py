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
        
