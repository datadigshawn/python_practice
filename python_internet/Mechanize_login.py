import mechanize
from bs4 import BeautifulSoup
import urllib2
from ntlm import HTTPNtlmAuthHandler

user = 'ECNT\\1848'
password = "Marchisio8"
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
print soup

