import socket
from threading import Thread
from trustlab.lab.trust_metrics import calc_trust_metrics
from trustlab.lab.artifacts.finalTrust import finalTrust
from trustlab.lab.config import Logging, get_current_time

untrustedAgents = []


class ClientThread(Thread):
    def run(self):
        try:
            msg = self.conn.recv(2048)
            reply = 'standard response'
            trust = 0
            node_log = self.id
            if node_log == 0:
                node_log = 'A'
            if node_log == 1:
                node_log = 'B'
            if node_log == 2:
                node_log = 'C'
            if node_log == 3:
                node_log = 'D'
            if node_log == 4:
                node_log = 'E'
            if node_log == 5:
                node_log = 'F'
            if node_log == 6:
                node_log = 'G'
            if node_log == 7:
                node_log = 'H'
            if msg != bytes('', 'UTF-8'):
                node_log_file_name = node_log + ".txt"
                node_log_path = Logging.LOG_PATH / node_log_file_name
                fos = open(node_log_path.absolute(), "ab+")
                current_message = str(msg)

                # The incoming message is split and added to the logfiles
                fos.write(
                    bytes(get_current_time() + ', connection from:', 'UTF-8') + bytes(current_message[2:3], 'UTF-8') +
                    bytes(', author:', 'UTF-8') + bytes(current_message[16:18], 'UTF-8') +
                    bytes(', tag:', 'UTF-8') + bytes(current_message[23:26], 'UTF-8') + bytes(',', 'UTF-8') +
                    bytes(str(self.scenario.instant_feedback[current_message[24:26]]), 'UTF-8') +
                    bytes(' |message:', 'UTF-8') + bytes(current_message[31:-1], 'UTF-8') +
                    bytes('| ', 'UTF-8') + bytes(reply, 'UTF-8') + bytes('\n', 'UTF-8'))

                fos.close()

                # Function call for the initialization of the trust values
                calc_trust_metrics(node_log, current_message, self.scenario)

                # Artifact finalTrust calculates the trust based on the saved values in the logfiles
                trust_value = finalTrust(node_log, current_message[2:3])

                # Adding the trustvalue to the trustlog
                trustlog_path = Logging.LOG_PATH / "trustlog.txt"
                fot = open(trustlog_path.absolute(), 'ab+')
                fot.write(
                    bytes(get_current_time() + ', node: ', 'UTF-8') + bytes(node_log, 'UTF-8') +
                    bytes(' trustvalue of node: ' + current_message[2:3], 'UTF-8') + bytes(' ' + trust_value, 'UTF-8') +
                    bytes('\n', 'UTF-8')
                )
                fot.close()
                print("_______________________________________")
                # print("_____________________" + trust_value + "-__________")

                if float(trust_value) < self.scenario.trust_thresholds['lower_limit']:
                    untrustedAgents.append(current_message[2:3])
                    print("+++" + node_log + ", nodes beyond redemption: " + current_message[2:3] + "+++")
                if float(trust_value) > self.scenario.trust_thresholds['upper_limit'] or float(trust_value) > 1:
                    self.scenario.authority.append(node_log[2:3])
                print("Node " + str(self.id) + " Server received data:", current_message[2:-1])
                print("_______________________________________")
            self.conn.send(bytes(str(reply), 'UTF-8'))
        except BrokenPipeError:
            pass
        return True

    def __init__(self, conn, id, port, scenario):
        Thread.__init__(self)
        self.conn = conn
        self.id = id
        self.port = port
        self.scenario = scenario


class AgentServer(Thread):
    def run(self):
        ip = '127.0.0.1'
        buffer_size = 2048

        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.bind((ip, self.port))

        while True:
            tcp_server.listen(4)
            print("Node server " + str(self.id) + " Waiting for connections from TCP clients...")
            (conn, (ip, port)) = tcp_server.accept()
            # TODO where is ID, an IP is added to ClientThread in original code
            new_thread = ClientThread(conn, self.id, port, self.scenario)
            new_thread.start()
            self.threads.append(new_thread)
            # self.threads = [thread for thread in self.threads if thread.is_alive()]

    def __init__(self, id, port, scenario):
        Thread.__init__(self)
        self.port = port
        self.id = id
        self.scenario = scenario
        self.threads = []


