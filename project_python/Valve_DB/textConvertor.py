# -*- coding: utf-8 -*-
import pyperclip
import array
import re
inch=[0.75,1,1.5,2,2.5,3,4,6,8,10,12]
minimeter=[20,25,40,50,65,75,100,150,200,250,300]
pasteVal=[]
"""
pyperclip.copy('The text to be copied to the clipboard.')
pyperclip.paste()
"""
#c=str(pyperclip.paste())
d=pyperclip.paste()
clipGet=d.rstrip().split('\r\n')
for c in clipGet:
    word=c.encode('utf-8')
    print re.findall('\d+', word)
    #inch
    wordMatch = re.search( '\d{1,3}["]', word)
    print word
    if wordMatch:
       print wordMatch.group()
       getinchNum = re.findall('\d+', word)
    else:
        #minimeter
        wordMatch2 = re.search( '\d{1,3}[Mm][Mm]|\d{1,3}[Aa]|\d{1,3}[∮]', word)
        if wordMatch2:
            print wordMatch2.group()
            getmmNum = re.findall('\d+', word)
            print getmmNum
            for numnum in getmmNum:
                
                floatNum = float(numnum)
                if floatNum in minimeter:
                    flag = minimeter.index(floatNum)
                    print "got cha"
                    print inch[flag]
        else:
            "not found"
print clipGet


