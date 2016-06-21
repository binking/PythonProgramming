#!/usr/bin/env python3
from email.mime.text import MIMEText # Multipurpose Internal Mail Extensions type
import email, smtplib

msg = MIMEText('This is Binking sending', 'plain', 'utf-8')
# Input user's address and password
from_addr = input('From: ')
password = input('Password: ')
# Input SMTP server address
smtp_server = input('SMTP server: ')
# Input receiver's address
to_addr = input('To: ')

server = smtplib.SMTP(smtp_server, 25) # 25, is default port of SMTP
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()