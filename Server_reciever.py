import socket

s = socket.socket()
print "Socket successfully created"
print s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

port = 55556

s.bind(('', port))
print "socket binded to %s" %(port)

s.listen(5)
print "socket is listening"

while True:
   c, addr = s.accept()
   intel = c.recv(100)
   substring = "letter:"
   if substring in intel:
       print intel[7:]
