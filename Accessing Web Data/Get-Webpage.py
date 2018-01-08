# Evan Douglass

# This program uses the socket library to gather metadata about a webpage

import socket

HOST = 'http://data.pr4e.org/intro-short.txt'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', PORT))
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode())

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
