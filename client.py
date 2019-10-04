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

        message = [None] * (messInfo[1])
        messDic[messInfo[0]] = message

        while True:
            mess = s.recv(messInfo[3])
            print(messInfo[2], "/", messInfo[1])
            message[messInfo[2] - 1] = mess.decode('UTF-8')
            if None not in message:
                break
            mess = s.recv(4)
            messInfo = []
            for c in mess:
                messInfo.append(c)
        output = ""
        for m in message:
            output += m

        print(output)
        s.close()
