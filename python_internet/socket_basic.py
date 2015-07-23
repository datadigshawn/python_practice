#FQDN = A fully qualified domain name
import socket
#get Host IP by Name
googleIP=socket.gethostbyname('google.com.hk')
#get Host Name n IP by Name
googleAll=socket.gethostbyname_ex('google.com.hk')
#get FQDN
GetFQDN= socket.getfqdn('google.com.hk')
#get My Name
MyHostName=socket.gethostname()
#get My LAN IP
MyHostIP=socket.gethostbyname(socket.gethostname())
#get My Name n LAN IP
MyHostIPnName=socket.gethostbyname_ex(socket.gethostname())
MyFQDN=socket.getfqdn()
#Get Host by Addr
GetHostbyAddr = socket.gethostbyaddr('172.16.48.103')

print "Google HK HOST IP is:/n", googleIP
print "Google HK HOST Name n IP is:/n", googleAll
print "Google FQDN is:\n", GetFQDN
print "\n"
print "My Host Name is:", MyHostName
print "My Host LAN IP is:", MyHostIP
print "My Host Name n LAN IP is:",  MyHostIPnName
print "My FQDN is:", MyFQDN
print "Get Host by Addr(172.16.48.103) is:\n", GetHostbyAddr
print "\n"
print  "Http Port Number:", socket.getservbyname('http')
print "SMTP, TCP port Number:", socket.getservbyname('smtp','tcp')
print  "Get 445 Port Name:", socket.getservbyport(445)
print  "Get 23 Port Name:", socket.getservbyport(23)
