# -*- coding: utf-8 -*-
from __future__ import division
import pyperclip
import array
import re
inch=[0.75,1,1.5,2,2.5,3,4,6,8,10,12]
millimeter=[20,25,40,50,65,75,100,150,200,250,300]
pasteVal=[]
class Vavle_Text:
    
        
    def Action(root,d):
        inch=[0.75,1,1.5,2,2.5,3,4,6,8,10,12]
        millimeter=[20,25,40,50,65,75,100,150,200,250,300]
        clipGet=d.rstrip().split('\r\n')
        getinchNum=[]
        inchArr=[]
        for c in clipGet:
            word=c.encode('utf-8')
            #inch fraction
            wordMatchF = re.search( '\d{1}[/]\d{1}["]|\d{0,1}\s\d{1}[/]\d{1}["]', word)
            wordMatch = re.search( '\d{1,3}["]', word)
            if wordMatchF:
                IntnFra = wordMatchF.group().split()   #separate int n fraction
                intcheck = len(IntnFra)
                if intcheck == 1:
                    fraNum = re.findall('\d+', IntnFra[0])
                    fraResult =  (int(fraNum[0])/int(fraNum[1]))
                if intcheck==2:
                    fraNum=re.findall('\d+',IntnFra[1])
                    fraResult = (int(IntnFra[0])+(int(fraNum[0])/int(fraNum[1])))
                inchArr.append(fraResult)
            else:
                #inch
                wordMatch = re.search( '\d{1,3}["]', word)
                if wordMatch:
                    inchNumString = re.findall('\d+', wordMatch.group())
                    for inchValue in inchNumString:
                        floatInchValue = float(inchValue)
                    inchArr.append(floatInchValue)
                #No inch in string   
                else:
                    #millimeter
                    wordMatch2 = re.search( '\d{1,3}[Mm][Mm]|\d{1,3}[Aa]|\d{2,3}[\^∮]', word)
                    if wordMatch2:
                        getmmNum = re.findall('\d+', wordMatch2.group())
                        #turn mm to float
                        for mmNumValue in getmmNum:      
                            mmValue = float(mmNumValue)
                        if mmValue in millimeter:
                            flag=millimeter.index(mmValue)
                            getinchNum = inch[flag]
                            inchArr.append(getinchNum)
                

                    else:
                        #Fraction
                        inchArr.append(0)

        return inchArr


