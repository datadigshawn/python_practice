import mechanize
from bs4 import BeautifulSoup
import urllib2
from ntlm import HTTPNtlmAuthHandler
from datetime import date, timedelta
import time
user = 'domain\\name'
password = "*******"
url = "http://www.ctci.com.tw/Acc_Rep/rate/rate.asp"
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
#print(response.read())
parser = response.read()
soup = BeautifulSoup(parser, "html.parser")
#print soup

#get today weekday

yWeekday = date.today().weekday()

wColor = ("#f4f5e7", "#eaf5ee")
count = 0  #can fit yesterday

for table in soup.findAll('table', align="left", border="0", cellpadding="3", cellspacing="0"):
    count += 1
    if count == yWeekday:
        print table
    """
for target in soup.findAll('tr', {'bgcolor':True}):
    #print target
    #print target['bgcolor']
    count += 1
for target1 in soup.findAll('tr', {'bgcolor':False}, height="30px"):
    #print target1
    target1
"""
# maybe for 1 weak (color) 






