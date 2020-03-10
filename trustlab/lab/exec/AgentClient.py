import socket
from threading import Thread
from datetime import datetime


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class AgentClient(Thread):
    def run(self):
        BUFFER_SIZE = 2000
        tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpClient.connect(('127.0.0.1', self.port))
        # send message
        tcpClient.send(bytes(self.msg, 'UTF-8'))
        rcvdata = tcpClient.recv(BUFFER_SIZE)
        # print("data sent at :"  + time.ctime(time.time()))
        rcvdata = rcvdata.decode()
        print(rcvdata)
        tcpClient.close()
        return True

    def __init__(self, ID, host, port, msg):
        Thread.__init__(self)
        self.ID = ID
        self.host = host
        self.port = port
        self.msg = msg




