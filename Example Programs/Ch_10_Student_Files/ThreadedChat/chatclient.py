"""
Author: Ken Lambert

Client for a chat room
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
print server.recv(BUFSIZE)

while True:
    message = raw_input('> ')
    if not message:
        break
    server.send(message + '\n')
    reply = server.recv(BUFSIZE)
    if not reply:
        print "Server disconnected"
        break
    print reply
server.close()
