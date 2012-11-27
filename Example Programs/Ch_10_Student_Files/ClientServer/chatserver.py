"""
Server for a chat room.  Handles one client at a 
time and participates in the conversation.
"""

from socket import *

HOST = 'localhost' 
PORT = 5000
ADDRESS = (HOST, PORT)
BUFSIZE = 1024

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:    print 'Waiting for connection . . .'    client, address = server.accept()    print '... connected from:', address    client.send('Welcome to my chat room!')  # Send greeting    while True:        message = client.recv(BUFSIZE)       # Reply from client        if not message:            print 'Client disconnected'            client.close()            break        else:            print message             client.send(raw_input('> '))     # Reply to client

