# -*- coding: utf-8 -*-
import urllib2
from HTMLParser import HTMLParser
from array import *
from Tkinter import *
import Tkinter as tk
import requests
import requests.auth
from bs4 import BeautifulSoup
from ntlm import HTTPNtlmAuthHandler
from datetime import date, timedelta
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ScrapingInfo:
    def __init__(root, Surl, TableID):
        root.Surl = Surl
        root.TableID = TableID
        root.HTMLdata = 0
        root.dataArr2GUI = []
    def GetHTMLCode(root):
        response = urllib2.urlopen(root.Surl)
        root.HTMLdata = response.read()
        #print data
    def ParserTarget(root):
        
        #Parse HTML CODE
        class MyHTMLParser(HTMLParser):
            def __init__(self):
                HTMLParser.__init__(self)
                self.tag = 0
                self.tableSelect = 0
                self.DataArr = []
                self.row = 0
                self.col = 0
            #Get the start tag content
            def handle_starttag(self, tags, attrs):
                #Target HTML Table 
                if tags == "table":
                    for name, value in attrs:
                        if name == 'id' and value == root.TableID:
                            self.tableSelect = 1
                if tags == "tr" and self.tableSelect == 1:
                    self.row += 1
            
                if tags == "td" and self.tableSelect == 1:
                    self.tag = "td"
                    self.col += 1
                    #print "Encountered a start tag:", tags
            
            #Get the end tag content
            def handle_endtag(self, tage):
                #check the target table end
                if tage == "table":
                    if self.tableSelect == 1:
                        self.tableSelect = 0
                if tage == "tr" and self.tableSelect == 1:
                    self.row += 1
                    self.col = 0
                
                if tage == "td" and self.tableSelect == 1:

                    tage
            
            #Get table's cell value
            def handle_data(self, content):
                if self.tag == "td" and self.tableSelect == 1:
                    #print "Encountered some data  :", content
                    self.DataArr.append([self.row, self.col, content])
                    root.dataArr2GUI = self.DataArr
                
        print root.dataArr2GUI
        # instantiate the parser and fed it some HTML
        parser = MyHTMLParser()
        #id = ctl00_ContentPlaceHolder1_priceGridView
        root.HTMLdata
        parser.feed(root.HTMLdata)
        
    def GUIresult(root):
        #print parser.DataArr
        #test for dynamic Frame
        
        GUI = Tk()


        DataFrame = Frame(GUI)
        DataFrame.grid(row=0, column=0)

        #header
        thead = ["日期", "匯率", "現貨\n最低", "現貨\n最高", "收盤價\n最低", "收盤價\n最高", "三個月\n期貨現貨\n最低", "三個月\n期貨現貨\n最高", "三個月\n期貨收盤價\n最低", "三個月\n期貨收盤價\n最高"]

        i = 0
        for Name in thead:
            i += 1
            EH = Label(DataFrame, font = "Helvetica 12", text=Name)
            EH.grid(row=0, column=i)
 

        def EntryInput(rowNum, colNum, text):
            textInput = StringVar()
        
            if colNum == 1:
                print text
                widthSet = 10
            else:
                widthSet = 6
       
            #data
            E1 = Entry(DataFrame, width=widthSet, font = "Helvetica 12 bold",  textvariable=textInput, state='readonly', borderwidth=0)
            E1.grid(row=rowNum, column=colNum)
            textInput.set(text)



        for name in root.dataArr2GUI:
            if name[1] == 10 and name[2].isdigit() == False:
                continue
                #print (name[0], name[1], name[2])
            else:
                #SelectedVal=Label(root, text=name[2]).grid(row=name[0], column=name[1])
                EntryInput(name[0],name[1],name[2])

        mainloop()
    

#END OF CLASSE
        
"""
OIL CLASSE
"""
class ScrapingOil:
    def __init__(root):
        root.DateArr = []
        root.PriceArr = []
    def WTexasOil(root):
        DA = []
        PA = []
        #Get website Information
        site= "http://web3.moeaboe.gov.tw/oil102/oil1022010/A00/Oil_Price2.asp"
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = requests.get(site, headers = hdr, verify = False)
        soup = BeautifulSoup(req.text, "html.parser")

        #Start Parser
        Idate = 0
        IPrice =0
        #Get the Date in the table
        for node in soup.findAll('td',align="center", width="8%"):
            Idate += 1
            DateVal = ''.join(node.findAll(text=True))
            #Put into Array
            if Idate >= 2 and Idate <=8:
                DA.append([(Idate-1), DateVal])
        #fetch data
        for node in soup.findAll('td',align="left", bgcolor="#FFFCF7", colspan="2"):
            stringT =  ''.join(node.findAll(text=True))
        for trfind in soup.findAll('tr', bgcolor="#ffffff"):
            
            #fetch price
            for tdNum in trfind.findAll('td', align="right"):
                IPrice +=1
                PriceVal = tdNum.find(text=True)
                #Put into Array
                if IPrice >=1 and IPrice <=7:
                    PA.append([IPrice, PriceVal])
        root.PriceArr = PA
        root.DateArr = DA



"""
END of OIL CLASSE 
"""

"""
LME Price
"""
class ScrapingLME:
    def __init__(root):
        #root.priceArr = []
        root.priceSelect = []
    def LMEselect(root):
        priceArr = []
        site= "https://www.lme.com/"
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = requests.get(site, headers = hdr, verify = False)
        soup = BeautifulSoup(req.text, "html.parser")
        price = soup.findAll('tr')
        for tr in price:
            for thRow in tr.findAll('td'):
                GotPrice = thRow.find(text=True)
                GotPrice = str(GotPrice)
                priceArr.append(GotPrice)
        root.priceSelect = [priceArr[3], priceArr[0], priceArr[5], priceArr[7]]
        
"""
END of LME Price
"""


"""
CURRENCY CLASSE
"""
class ScrapingCurrency:
    def __init__(root):
        root.CResultArr = []
    def CurrencySelect(root):
        user = 'DOMAIL\\USRNAME'
        password = "PASSWORD"
        url = "WEBSITE"
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, user, password)
        # create the NTLM authentication handler
        auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
        # create and install the opener
        opener = urllib2.build_opener(auth_NTLM)
        urllib2.install_opener(opener)
        data="""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" >
        <soapenv:Header/>
        <soapenv:Body>
        <ns:FromTimestamp>2012-05-10</ns:FromTimestamp>
        </soapenv:Body>
        </soapenv:Envelope>
        """
        headers={"SOAPAction":"SomeSoapFunc","Content-Type":"text/xml;charset=UTF-8"}
        req = urllib2.Request(url, data, headers)
        response=urllib2.urlopen(req)
        # retrieve the result
        parser = response.read()
        soup = BeautifulSoup(parser, "html.parser")
        #get today weekday
        yWeekday = date.today().weekday()
        cc = (1, 17, 4, 13)
        count = 0  #can fit yesterday
        t = 0
        for table in soup.findAll('table', align="left", border="0", cellpadding="3", cellspacing="0"):
            count += 1
            if count == yWeekday:
                #list the currency 
                for title in table.findAll('td', {'class':'DET2'}):
                    t += 1
                    #choose the currency from cc USD JPY EUR CNY
                    for checkcc in cc:
                        if ((checkcc*5)-3) == t:
                            Cvalue = title.text
                            root.CResultArr.append(Cvalue)
"""
END of CURRENCY CLASSE
"""

"""
LME LOGIN
"""
class ScrapingLMELogin:
    def __init__(root):
        root.LMELogin = []
    def LoginGetValue(root):
        #login
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        driver = webdriver.PhantomJS()
        driver.get("https://secure.lme.com/Data/Community/Login.aspx")
        driver.find_element_by_id('_logIn__userID').send_keys("USERNAME")
        driver.find_element_by_id('_logIn__password').send_keys("PASSWORD")
        driver.find_element_by_id('_logIn__logIn').click()
        #enter the page
        driver.find_element_by_id('_subMenu__dailyStocksPricesMetals').click()
        date = driver.find_element_by_xpath("//*[@id='Table3']/tbody/tr[5]/td/table/tbody/tr[6]/td[1]").text
        
        Copper = driver.find_element_by_xpath("//*[@id='Table3']/tbody/tr[5]/td/table/tbody/tr[7]/td[8]").text
        Aluminium = driver.find_element_by_xpath("//*[@id='Table3']/tbody/tr[5]/td/table/tbody/tr[7]/td[6]").text
        Nickel = driver.find_element_by_xpath("//*[@id='Table3']/tbody/tr[5]/td/table/tbody/tr[7]/td[12]").text
        Zinc = driver.find_element_by_xpath("//*[@id='Table3']/tbody/tr[5]/td/table/tbody/tr[7]/td[16]").text
        #print date
        #print Copper, Aluminium, Nickel, Zinc
        date1 = date.encode("utf-8")
        
        dateConvert = ("%s-%s-%s"%(date1[11:], date1[8:10], date1[5:7]))
        #print dateConvert
        driver.quit()
        LMELogin = (dateConvert, Copper.encode('utf-8'), Aluminium.encode('utf-8') ,Nickel.encode('utf-8'), Zinc.encode('utf-8'))
        return LMELogin
    
"""
END OF LME LOGIN
"""

