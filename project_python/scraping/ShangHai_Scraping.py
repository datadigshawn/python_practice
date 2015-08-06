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
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth
priceArr = []
siteHome = "http://market.cnal.com/changjiang/"
site= "http://market.cnal.com/changjiang/2015/07-31/1438310372411596.shtml"
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'}

reqHome = requests.get(siteHome, headers = hdr)
soupHome = BeautifulSoup(reqHome.text, "html.parser")
for ul in soupHome.find_all('ul', {"class": "obj-market-list"}):
   for atag  in ul.find_all('a'):
      print(atag.get('href'))
  

req = requests.get(site, headers = hdr)
print req.status_code
#page = urllib2.urlopen(req)

soup = BeautifulSoup(req.text, "html.parser")

for table in soup.findAll('table', {"id": "jsxq_view"}):
  for tr in table.findAll('tr', bgcolor='#f4f4ff'):
    #print tr
    for td in tr.findAll('td'):
      print td
    


