import socket

class ReceiveMessages:
	def WaitForMessage(self):
		s = socket.socket()
		host = "72.79.65.14"
		port = 697
		receivedMessage = []

		while True:
			s.connect((host, port))
			receivedMessage.append(s.accept(1024))
			s.close()