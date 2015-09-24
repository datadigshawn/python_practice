# -*- coding: utf-8 -*-
from __future__ import division
from collections import Counter
import pyperclip
import array
import re
SpaceArr=[]
KeySpaceArr=[]
ValSpaceArr=[]

DueArr=[]
TreArr=[]
QuattroArr=[]
KeyDueArr=[]
ValDueArr=[]
import sqlite3 as lite
import os
import datetime, time
print datetime.datetime.now()
dstroot="C:\\temp_read_Excel"
os.chdir(dstroot)
"""
con = lite.connect('database.db')
with con:
    cur=con.cursor()
    search="SELECT * FROM excel_content WHERE Cell_Data ='價格'"
    add_tag="UPDATE excel_file SET Title_Row=? WHERE ID=?"
    check_havetag="SELECT * FROM excel_file WHERE ID=? and Title_Row!='NULL'"
    for result in con.execute(search):
        check_para=[result[1]]
        
        for checker in con.execute(check_havetag,check_para):
            print "exist"
            break
        else:
            tag_para=[result[2],result[1]]
            con.execute(add_tag,tag_para)
print datetime.datetime.now()

"""
Data_fetchArr=[]
con = lite.connect('database.db')
with con:
    cur=con.cursor()
    get_cell="SELECT Cell_Data From excel_content WHERE ID>80000 and ID<=90000"
    #850985
    for c in con.execute(get_cell):
        Data_fetchArr.append(c[0])
    
    

for cells in Data_fetchArr:
    
    #space
    Spacewords=cells.rstrip().split(' ')
    for spaceword in Spacewords:
        if spaceword!='':
            SpaceArr.append(spaceword)
    #due word
    Due=re.findall(r'.{1,2}',cells,re.DOTALL)
    for DueW in Due:
        DueArr.append(DueW)
    #tre word
    Tre=re.findall(r'.{2,3}',cells,re.DOTALL)
    for TreW in Tre:
        TreArr.append(TreW)
    #Quattro word
    Quattro=re.findall(r'.{3,4}',cells,re.DOTALL)
    for QuattroW in Quattro:
        QuattroArr.append(QuattroW)


KeySpaceArr = Counter(SpaceArr).keys()
ValSpaceArr = Counter(SpaceArr).values()
KeyDueArr= Counter(DueArr).keys()
ValDueArr= Counter(DueArr).values()
KeyTreeArr= Counter(TreArr).keys()
ValTreArr= Counter(TreArr).values()
KeyQuattroArr= Counter(QuattroArr).keys()
ValQuattroArr= Counter(QuattroArr).values()

print datetime.datetime.now(), "mining"
con2 = lite.connect('chinese_dictionary.db')
with con2:
    cur=con2.cursor()
    check_word = 'SELECT * From dictionary WHERE Word=?'
    update_word = 'UPDATE dictionary SET Times=? WHERE ID=?'
    insert_word = 'INSERT INTO dictionary(Word,Times) VALUES (?,?)'
    i=0
    for Sapce in KeyQuattroArr:
        i+=1
        Word=Sapce
        Times=int(ValQuattroArr[i-1])
        
        check_para=[Word]
        for checker in con2.execute(check_word,check_para):
            update_para=[int(checker[2])+Times,checker[0]]
            con2.execute(update_word,update_para)
            break
        else:
            insert_para=[Word,Times]
            con2.execute(insert_word,insert_para)

    i=0
    for Sapce in KeyTreeArr:
        i+=1
        Word=Sapce
        Times=int(ValTreArr[i-1])
        
        check_para=[Word]
        for checker in con2.execute(check_word,check_para):
            update_para=[int(checker[2])+Times,checker[0]]
            con2.execute(update_word,update_para)
            break
        else:
            insert_para=[Word,Times]
            con2.execute(insert_word,insert_para)

    i=0
    for Sapce in KeyDueArr:
        i+=1
        Word=Sapce
        Times=int(ValDueArr[i-1])
        
        check_para=[Word]
        for checker in con2.execute(check_word,check_para):
            update_para=[int(checker[2])+Times,checker[0]]
            con2.execute(update_word,update_para)
            break
        else:
            insert_para=[Word,Times]
            con2.execute(insert_word,insert_para)

    i=0
    for Sapce in KeySpaceArr:
        i+=1
        Word=Sapce
        Times=int(ValSpaceArr[i-1])
        
        check_para=[Word]
        for checker in con2.execute(check_word,check_para):
            update_para=[int(checker[2])+Times,checker[0]]
            con2.execute(update_word,update_para)
            break
        else:
            insert_para=[Word,Times]
            con2.execute(insert_word,insert_para)
"""
i=0
for Dsapce in KeyDueArr:
    i+=1
    print Dsapce.encode('utf-8'), ValDueArr[i-1]

"""
print datetime.datetime.now() ,"end"
