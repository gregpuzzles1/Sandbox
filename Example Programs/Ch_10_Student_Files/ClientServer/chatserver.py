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

while True:
