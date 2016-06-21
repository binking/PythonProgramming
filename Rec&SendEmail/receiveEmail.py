import poplib
emailServer = poplib.POP3('pop3.163.com')
emailServer.user('18813105413@163.com')
emailServer.pass_('qwertyuiop')

# Print welcome message
serverWelcome = emailServer.getwelcome()
print (serverWelcome)

# Keep connection
emailServer.noop()
# Get number and length of emails
emailMsgNum, emailSize = emailServer.stat()
print ('email number is %d and size is %d' % (emailMsgNum, emailSize))
emailServer.retr(1)
emailServer.list(1)
for i in range(emailMsgNum):
    for piece in emailServer.retr(i+1)[1]:
        if piece.startswith('Subject'):
            print ('\t' + piece)
            break