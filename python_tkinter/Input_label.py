import sys
from tkinter import *
def mhello():
    mtext = meant.get()
    mlabel2 = Label(mGui,text=text).pack()
    return

mGui = Tk()
meant = StringVar()

mGui.geometry(450*450+500+309)
mGui.title('title')

mlabel = Label(mGui,text = 'my label').pack()

mbutton = Button(mGui,text = 'OK', command = mhello, fg = 'red', bg = 'blue').pack()

mEntry = Entry(mGui, textvariable=ment).pack
