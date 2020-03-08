import socket
from threading import Thread
from datetime import datetime

untrustedAgents = []

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ClientThread(Thread):
    def run(self):
        try:
            msg = self.conn.recv(2048)
            reply = ''
            trust = 0
            nodelog = self.id
            if nodelog == 0:
                nodelog = 'A'
            if nodelog == 1:
                nodelog = 'B'
            if nodelog == 2:
                nodelog = 'C'
            if nodelog == 3:
                nodelog = 'D'
            if nodelog == 4:
                nodelog = 'E'
            if nodelog == 5:
                nodelog = 'F'
            if nodelog == 6:
                nodelog = 'G'
            if nodelog == 7:
                nodelog = 'H'
            if msg != bytes('', 'UTF-8'):

                fos = open(nodelog + ".txt", "ab+")
                logrecord = str(msg)

                ###Function call for the initialization of the trust values
                trust_initialization(nodelog, logrecord)

                ###The incoming message is split and added to the logfiles
                fos.write(
                    bytes(get_current_time() + ', connection from:', 'UTF-8') + bytes(logrecord[2:3], 'UTF-8') +
                    bytes(', author:', 'UTF-8') + bytes(logrecord[16:18], 'UTF-8') +
                    bytes(', tag:', 'UTF-8') + bytes(logrecord[23:26], 'UTF-8') + bytes(',', 'UTF-8') +
                    bytes(str(INSTANTFEEDBACK[logrecord[24:26]]), 'UTF-8') +
                    bytes(' |message:', 'UTF-8') + bytes(logrecord[31:-1], 'UTF-8') + bytes('| ', 'UTF-8') +
                    bytes(reply, 'UTF-8') + bytes('\n', 'UTF-8'))

                fos.close()

                ###Artifact finalTrust calculates the trust based on the saved values in the logfiles
                trustEx = finalTrust(nodelog, logrecord[2:3])

                ###Adding the trustvalue to the trustlog
                fot = open('trustlog.txt', 'ab+')
                fot.write(
                    bytes(get_current_time() + ', node: ', 'UTF-8') + bytes(nodelog, 'UTF-8') +
                    bytes(' trustvalue of node: ' + logrecord[2:3], 'UTF-8') + bytes(' ' + trustEx, 'UTF-8') +
                    bytes('\n', 'UTF-8')
                )
                fot.close()
                print("_______________________________________")
                # print("_____________________" + trustEx + "-__________")

                if float(trustEx) < -0.75:  # TRUSTTHRESHOLD['LowerLimit']:
                    untrustedAgents.append(logrecord[2:3])
                    print("+++" + nodelog + ", nodes beyond redemption: " + logrecord[2:3] + "+++")
                if float(trustEx) > 0.75 or float(trustEx) > 1:  # TRUSTTHRESHOLD['UpperLimit']:
                    AUTHORITY.append(nodelog[2:3])
                print("Node " + str(self.id) + " Server received data:", logrecord[2:-1])
                print("_______________________________________")
            self.conn.send(bytes(str(reply), 'UTF-8'))

        except BrokenPipeError:
            pass

    def __init__(self, conn, id, port):
        Thread.__init__(self)
        self.conn = conn
        self.id = id
        self.port = port


class AgentServer(Thread):
    def run(self):
        ip = '0.0.0.0'
        BUFFER_SIZE = 2048

        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((ip, self.port))
        threads = []

        while True:
            tcpServer.listen(4)
            print("Node server " + str(self.id) + " Waiting for connections from TCP clients...")
            (conn, (ip, port)) = tcpServer.accept()
            # TODO where is ID, an IP is added to CLientThread
            newthread = ClientThread(conn, ip, port)
            newthread.start()
            threads.append(newthread)

        for t in threads:
            t.join()

    def __init__(self, id, port):
        Thread.__init__(self)
        self.port = port
        self.id = id


