import mechanize

br = mechanize.Browser()
"""
br.open("http://www.taiwancable.org.tw/Member.aspx")
#List the forms
for form in br.forms():
    print "Form name:", form.name
    print form


br.select_form("aspnetForm")

br.form['ctl00$ContentPlaceHolder1$nameTextBox'] = 'HA'
#ctl00$ContentPlaceHolder1$queryImageButton
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


