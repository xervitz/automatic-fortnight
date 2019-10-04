import socket
from parseMessages import ParseMessages


class ReceiveMessages:
    @staticmethod
    def WaitForMessage(host="", port=697):
        s = socket.socket()
        host = "72.79.65.14"
        port = 697
        s.connect((host, port))
        mess = s.recv(1024)
        ParseMessages.Parse(mess)
        s.close()
