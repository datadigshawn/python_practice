import os
from nt import chdir
import subprocess
srcfilePath=os.path.join('C:\\', 'Python2.7.10','project_database','excel_database')
fileName='123.msg'
def MsgToExcelDatabase(srcfilePath,fileName):
    MailmsgPath=os.path.join(srcfilePath,fileName)
    #start extract attachment from 123.msg
    DIR = os.path.join('C:\\', 'Python2.7.10', 'msg-extractor-master', 'ExtractMsg.py')
    subprocess.call(['python', DIR, MailmsgPath])

MsgToExcelDatabase(srcfilePath,fileName)
