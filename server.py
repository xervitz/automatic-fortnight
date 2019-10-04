from socket import *
import _thread as thread


def start_up():
    global slist
    PORT_NUMBER = 697
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((get_ip_address(), PORT_NUMBER))
    s.listen(0)
    client,  address = s.accept()
    data = "hello"
    client.send(data.encode('utf-8'))
    client.close()
    s.close()


def get_ip_address():  # using google to obtain real ip, google most reliable host I know.
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def listen(s):
    while True:
        l = int_from_bytes(s.recv(1))
        emsg = s.recv(l)
        msg=emsg.decode('utf-8')
        if len(msg)>0:
            thread.start_new_thread(parse,(msg,s,))
        else:
            pass


start_up()