
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import json
from datetime import datetime, timedelta

today = datetime.now().date()


with open("e_mail_credentials.json", "r") as file:
    creds = json.load(file)

e_mail = creds["Email_Address"]
passwd = creds["Password"]
to = creds["To"]
smtp = smtplib.SMTP('smtp.gmail.com', 587) 
smtp.ehlo() 
smtp.starttls() 
smtp.login(e_mail, passwd)

with open("episodes_to_watch.txt", "r") as file:
    content = file.read()

msg = MIMEMultipart() 
msg['Subject'] = "Yeni eklenen bölümler" 
msg.attach(MIMEText(content))

try:
    smtp.sendmail(from_addr="Your Login Email", to_addrs=to, msg=msg.as_string()) 
    print("email sent succesfully. Date : "+ str(today))
except:
    print("a problem occured while sending mail")