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

print server.recv(BUFSIZE)       # The server's greetingwhile True:    message = raw_input('> ')    # Get my reply or quit    if not message:        break    server.send(message + '\n')  # Send my reply to the server    reply = server.recv(BUFSIZE) # Get the server's reply    if not reply:
        print "Server disconnected"        break    print reply                  # Display the server's replyserver.close()