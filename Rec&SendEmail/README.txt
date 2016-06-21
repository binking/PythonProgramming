Libraries :
	poplib	http://docs.python.org/library/poplib.html

	imaplib	https://docs.python.org/2/library/imaplib.html

	email

Someone said, if you repeat the task more than three times, just automate it by script.
邮箱 POP3服务器（端口110） SMTP服务器（端口25） 
qq.com pop.qq.com smtp.qq.com 
SMTP是发送邮件的协议，Simple Message Transfer Protocol
Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件

Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。