"""
Author: Ken Lambert

Server for a therapy session.  Handles one
client at a time.
"""

from socket import *
from doctor import Doctor

HOST = 'localhost'
PORT = 21567
ADDRESS = (HOST, PORT)
BUFSIZE = 1024

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print 'Waiting for connection . . .'
    client, address = server.accept()
    print '... connected from:', address
    dr = Doctor()
    client.send(dr.greeting())

    while True:
        message = client.recv(BUFSIZE)
        if not message:
            print 'Client disconnected'
            client.close()
            break
        else:
            client.send(dr.reply(message))

server.close()


