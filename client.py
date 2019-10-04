import socket
from parseMessages import ParseMessages

class ReceiveMessages:
	@staticmethod
	def WaitForMessage(host="", port=697):
		s = socket.socket()
		host = "72.79.65.14"
		port = 697

		while True:
			s.connect((host, port))
			ParseMessages.Parse(s.recv(1024))
			s.close()
