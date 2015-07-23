import sys
from tkinter import *
def mhello():
    mtext = ment.get()
    mlabel2 = Label(mGui, text=mtext).pack()
    return

mGui = Tk()
ment = StringVar()

mGui.geometry('450x450+500+300')
mGui.title('title')

mlabel = Label(mGui, text = 'My label').pack()

mbutton = Button(mGui, text = 'OK', command = mhello, fg = 'red', bg = 'blue').pack()

mEntry = Entry(mGui, textvariable = ment).pack()
