import urllib2
from HTMLParser import HTMLParser
from array import *
import requests
import requests.auth
from bs4 import BeautifulSoup
from ntlm import HTTPNtlmAuthHandler




user = 'Domain\\Username'
password = "your password"
url = "your url"
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

parser = response.read()
#use beautifulsoup 
soup = BeautifulSoup(parser, "html.parser")

                   

for div in soup.findAll('div'):
    print div

