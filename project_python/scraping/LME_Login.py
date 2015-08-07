import mechanize
import urllib

site = "https://secure.lme.com/Data/Community/Login.aspx"
br = mechanize.Browser()

#br.set_cookiejar(cookie)
br.set_handle_robots( False )
br.addheaders = [
    ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'),
    ('Cache-Control', 'max-age=0'),
    ('Referer', 'https://secure.lme.com/Data/Community/Login.aspx'),
    ('Accept-Encoding', 'gzip, deflate'),
    ('Accept-Language', 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4'),
    ('Cache-Control','max-age=0'),
    ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
    ('Connection','keep-alive'),
    ('Content-Length','3636'),
    ('Content-Type','application/x-www-form-urlencoded'),
    ('Upgrade-Insecure-Requests','1')
]
#br.select_form(nr=0)
#br.form.set_all_readonly(False)

response = br.open(site)

print response
