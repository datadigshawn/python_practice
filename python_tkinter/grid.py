from Tkinter import *
import os
import re
import sets

from array import *

root = Tk()
Arr = ([0, 1, "0-1"], [1, 1, "1-1"], [2, 2, "2-2"])
for place in Arr:
    print place[0], place[1], place[2]
    SelectedVal=Label(root, text=place[2]).grid(row=place[0], column=place[1])
mainloop()
