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

        while True:
            mess = s.recv(4)
            messInfo = []
            for c in mess:
                messInfo.append(c)

            if len(messInfo) != 4:
                print("Invalid message received")
                continue

            if messInfo[0] not in messDic:
                message = [None] * (messInfo[1])
                messDic[messInfo[0]] = message

            mess = s.recv(messInfo[3])
            print(messInfo[2], "/", messInfo[1], " Message ID: ", messInfo[0])
            messDic[messInfo[0]][messInfo[2] - 1] = mess.decode('UTF-8')
            if None not in messDic[messInfo[0]]:
                break

        output = ""
        for key in messDic:
            for m in messDic[key]:
                output += m
            output += "\n"

        print(output)
        s.close()
