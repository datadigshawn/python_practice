from urllib2 import urlopen
mypublicIP = urlopen('http://ip.42.pl/raw').read()
print mypublicIP
