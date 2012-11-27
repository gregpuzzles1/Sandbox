"""
Client for a multi-client chat room.
"""

from socket import *

HOST = 'localhost'
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
print server.recv(BUFSIZE)
name = raw_input('Enter your name: ')
server.send(name)

while True:
    record = server.recv(BUFSIZE)
    if not record:
        print "Server disconnected"
        break
    print record
    message = raw_input('> ')
    if not message:
        break
    server.send(message + '\n')
server.close()
