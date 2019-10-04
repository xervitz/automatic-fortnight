import socket

s = socket.socket()
host = 72.79.65.14
port = 25565

s.connect((host, port))
print s.recv(1024)
s.close()