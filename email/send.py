from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import sys


if len(sys.argv) > 1:
    fileName = sys.argv[1]
    if fileName != None:
        print(fileName)

        from_addr = "dicking02@126.com"
        password = "cloud311"
        to_addr = "zhangdong123@loocha.com"
        smtp_server = "smtp.126.com"

        msg = MIMEMultipart('related')  
        msg['Subject'] = 'android_apk_' + fileName
        msg['From'] = from_addr
        msg['To'] = to_addr

        msg.attach(MIMEText('send apks','plain','utf-8'))


        att = MIMEText(open('C:\\zdnuist\\work_svn\\v5.3_R\\LoochaCampus\\build\\outputs\\apk\\'+fileName, 'rb').read(), 'base64', 'utf-8')  
        att["Content-Type"] = 'application/octet-stream'  
        att["Content-Disposition"] = 'attachment; filename="'+fileName+'"'  
        msg.attach(att) 

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
