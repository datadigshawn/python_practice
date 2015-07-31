# -*- coding: utf-8 -*-
import urllib2, sys
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from array import *
from Tkinter import *
import Tkinter as tk
import requests
import requests
import requests.auth

priceArr = []
      
site= "https://www.lme.com/"
hdr = {'User-Agent': 'Mozilla/5.0'}


req = requests.get(site, headers = hdr, verify = False)
#page = urllib2.urlopen(req)

soup = BeautifulSoup(req.text, "html.parser")
#print soup


price = soup.findAll('tr')
for tr in price:
  
  for thRow in tr.findAll('td'):
    GotPrice = thRow.find(text=True)
    GotPrice = str(GotPrice)
    priceArr.append(GotPrice)
print priceArr[3], priceArr[0], priceArr[5], priceArr[7]
priceSelect = [priceArr[3], priceArr[0], priceArr[5], priceArr[7]]
print priceSelect
