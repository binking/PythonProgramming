#!/usr/bin/env python3

import poplib
from email import parser

#pop_conn = poplib.POP3_SSL('pop.gmail.com')
#pop_conn.user('jiangzhibin2014.xujie@gmail.com')
#pop_conn.pass_('jzbwymxjno1_gmail'.encode())

pop_conn = poplib.POP3_SSL('pop.163.com')
pop_conn.user('18813105413@163.com')
pop_conn.pass_('qwertyuiop')

# Get messages from server
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
print(len(messages))
# Concat message pieces
messages = [b"\n".join(msg[1]).decode() for msg in messages]
messages = [parser.Parser().parsestr(msg) for msg in messages]
# Parsing email into an email object
for msg in messages:
    print(msg['subject'])
    body = msg.get_payload(decode = True)
    if type(body) != None :
        print(body.decode())
pop_conn.quit()