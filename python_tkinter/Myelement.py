from Tkinter import *
def EntryIn(row, col, text, frameName):

    InputE = StringVar()
    EOil = Entry(frameName, width=10, font = "Helvetica 8",  textvariable=InputE, state='readonly', borderwidth=0)
    EOil.grid(row=row, column=col)
    InputE.set(text)



root = Tk()
root.geometry('500x500+500+300')
F1 = Frame(root)
F1.grid(row=0, column=0)
for
EntryIn(1,1,'hello',F1)
mainloop()
