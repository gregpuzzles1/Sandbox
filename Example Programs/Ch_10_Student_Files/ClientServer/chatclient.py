"""
Client for a chat room.
"""

from socket import *

HOST = 'localhost' 
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)

print server.recv(BUFSIZE)       # The server's greeting
        print "Server disconnected"