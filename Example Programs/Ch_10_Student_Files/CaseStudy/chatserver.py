"""
Server for a multi-client chat room.  
"""

from socket import *
from chatrecord import ChatRecord
from threading import Thread
from time import ctime

class ClientHandler(Thread):
    
    def __init__(self, client, record):
        Thread.__init__(self)
        self._client = client
        self._record = record

    def run(self):
        self._client.send('Welcome to the chat room!')
        self._name = self._client.recv(BUFSIZE)
        self._client.send(str(self._record))
        while True:
            message = self._client.recv(BUFSIZE)
            if not message:
                print 'Client disconnected'
                self._client.close()
                break
            else:
                message = self._name + ' ' + \
                          ctime() + '\n' + message
                self._record.add(message)
                self._client.send(str(self._record))


HOST = 'localhost'
PORT = 5000
ADDRESS = (HOST, PORT)
BUFSIZE = 1024

record = ChatRecord()
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print 'Waiting for connection . . .'
    client, address = server.accept()
    print '... connected from:', address
    handler = ClientHandler(client, record)
    handler.start()


