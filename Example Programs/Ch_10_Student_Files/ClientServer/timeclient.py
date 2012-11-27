"""
Client for obtaining the day and time.
"""

from socket import *

HOST = 'localhost' 
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)   # Create a socket
server.connect(ADDRESS)                 # Connect it to a host
dayAndTime = server.recv(BUFSIZE)       # Read a string from it
print dayAndTime
server.close()                          # Close the connection
