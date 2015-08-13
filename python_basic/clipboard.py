import pyperclip
"""
pyperclip.copy('The text to be copied to the clipboard.')
pyperclip.paste()
"""
c=str(pyperclip.paste())
d=pyperclip.paste()
g=c.rstrip().split('\r\n')
f=c.decode('unicode_escape')
print g
