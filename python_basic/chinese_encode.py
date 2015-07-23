#Chinese Encode Decode 
#!/usr/bin/python  
#coding=utf-8
#str
strString='中文'  
print "strString is:",type(strString)  
print strString  
#unicode
uniString=u"中文"  
print "uniString is:",type(uniString)  
print uniString  
#encode GBK
gbkString=uniString.encode("gbk")  
print "gbkString is:",type(gbkString)  
print gbkString  
#decode GBK 
gbkgbkString=gbkString.decode("gbk")  
print "gbkgbkString is:",type(gbkgbkString)
print gbkgbkString

#decode utf-8 
StrCode = 'ICM \xe8\xa8\x88\xe8\xb2\xbb\xe9\x9b\xbb\xe9\x8c\xb6'
StrDEUtf8String = StrCode.decode('utf-8')
print type(StrCode), " [decode utf-8]  =>",type(StrDEUtf8String)
print StrDEUtf8String


#encode utf-8
utfutfString=StrDEUtf8String.encode("utf-8")
print type(StrDEUtf8String), " [encode utf-8]  =>", type(utfutfString)
print utfutfString
