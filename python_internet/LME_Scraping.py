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
from pyquery import PyQuery


priceArr = []
      
site= "https://secure.lme.com/Data/Community/Login.aspx"
hdr = {'User-Agent': 'Mozilla/5.0'}
s = requests.Session()
login_data = {
    '_logIn:_userID': 'raykuo',
    '_logIn:_password': 'InkL3#c7'
}
req1 = s.post(site, data=login_data)
req = requests.get(site, headers = hdr, verify = False)
#page = urllib2.urlopen(req)

soup = BeautifulSoup(req1.text, "html.parser")
print soup



