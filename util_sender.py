import socket
import sys
s = socket.socket()
port = 55556
s.connect(('192.168.100.6', port))
s.send('letter:' + sys.argv[1])
s.close()
