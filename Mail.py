'''
Send an Email from sender to Receiver using Python
Email contains Title and Message.
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content='''Hello Sir/Madam,
I'm Suresh Bhatia from WIT Sangli, expecting a bonafide
certificate for Adhaar card registration.

Thank you,
Suresh.'''
sender_address="sender@gmail.com"
sender_pass="password"

receiver_address="receiver@gmail.com"

message=MIMEMultipart()
message['From']=sender_address
message['To']=receiver_address
message['Subject']="A TEST EMAIL"
message.attach(MIMEText(mail_content,'plain'))
session=smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login(sender_address,sender_pass)
text=message.as_string()
session.sendmail(sender_address,receiver_address,text)
session.quit()  #logout
