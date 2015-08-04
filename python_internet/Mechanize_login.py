import mechanize


"""
br = mechanize.Browser()
br.open("http://www.taiwancable.org.tw/Member.aspx")
#List the forms
for form in br.forms():
    print "Form name:", form.name
    print form


br.select_form("aspnetForm")

br.form['ctl00$ContentPlaceHolder1$nameTextBox'] = 'HA'
#ctl00$ContentPlaceHolder1$queryImageButton
"""
"""
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)  
br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')]
#User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36
try:
    br.add_password('http://cccec.eandc.com.tw/portal/', 'ECNT\1848', 'Marchisio8')
    response = mechanize.urlopen("http://portal.globaltransit.net/")
except mechanize.HTTPError, response:
    pass

body = response.read()
print body
br.add_password('http://cccec.eandc.com.tw/portal/', 'ECNT\1848', 'Marchisio8')
br.open('http://cccec.eandc.com.tw/portal/')

"""
"""
#from mechanize import Browser


USERNAME = "ECNT\1848"
PASSWORD = "Marchisio8"
LOGIN_PAGE = "http://cccec.eandc.com.tw"

browser = mechanize.Browser()

browser.set_handle_robots(False)
browser.set_handle_refresh(False)
#br.add_password(LOGIN_PAGE, USERNAME, PASSWORD)
browser.open( LOGIN_PAGE )

browser.select_form( nr=0 )
#browser.select_form("viewport")
browser['username'] = USERNAME
browser['password'] = PASSWORD
response = browser.submit()
print response.read()
"""
import urllib2
from ntlm import HTTPNtlmAuthHandler

user = 'ECNT\1848'
password = "Marchisio8"
url = "http://cccec.eandc.com.tw"

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, user, password)
# create the NTLM authentication handler
auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

# create and install the opener
opener = urllib2.build_opener(auth_NTLM)
urllib2.install_opener(opener)

# retrieve the result
response = urllib2.urlopen(url)
print(response.read())
