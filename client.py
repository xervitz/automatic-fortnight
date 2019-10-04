import socket

class RecieveMessages:
	def 
	s = socket.socket()
	host = "72.79.65.14"
	port = 697
	recievedMessage = []

	while True:
		s.connect((host, port))
		recievedMessage.append(s.accept(1024))
		s.close()