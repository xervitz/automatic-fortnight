from socket import *
import time
import _thread as thread
MSGID = 1



def get_id():
    global MSGID
    id = MSGID
    MSGID += 1
    return id


def start_up():
    global slist
    PORT_NUMBER = 697
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((get_ip_address(), PORT_NUMBER))
    s.listen(0)
    client,  address = s.accept()
    data = "hello"
    send_message(client, "Hello")
    time.sleep(1)
    s.close()


def get_ip_address():  # using google to obtain real ip, google most reliable host I know.
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


#128, first 16 are info
def send_message(s, message):
    data = message.encode('utf-8')
    length = (len(data))
    messages = (length // (128-12)) + 1
    id = get_id()
    info = int_to_bytes(id) + int_to_bytes(messages)
    for i in range(messages):
        i_info = info + int_to_bytes(i + 1)
        data = i_info + message.encode('utf-8')
        s.send(data)
    return


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')


#send_message(None, "hello")
start_up()
