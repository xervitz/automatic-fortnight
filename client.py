import socket
from parseMessages import ParseMessages


class ReceiveMessages:
    @staticmethod
    def WaitForMessage(host="", port=697):
        s = socket.socket()
        host = "72.79.65.14"
        port = 697
        messDic = {}

        s.connect((host, port))

        mess = s.recv(4)

        messInfo = []
        for c in mess:
            messInfo.append(c)

        message = [None] * messInfo[1]
        messDic[messInfo[0]] = message

        while message.__contains__(None):
            mess = s.recv(messInfo[3])
            messDic[messInfo[0]][messInfo[2]] = mess
            mess = s.recv(4)
            messInfo = []
            for c in mess:
                messInfo.append(c)

        for m in messDic[1]:
            print(m)

        s.close()
