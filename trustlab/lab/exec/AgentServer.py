import socket
from threading import Thread
from trustlab.lab.trust_metrics import calc_trust_metrics
from trustlab.lab.artifacts.finalTrust import final_trust
from trustlab.lab.config import Logging, get_current_time

untrustedAgents = []


class ClientThread(Thread):
    def run(self):
        try:
            msg = self.conn.recv(2048)
            reply = 'standard response'
            # trust = 0
            # current_agent = self.id
            # if current_agent == 0:
            #     current_agent = 'A'
            # if current_agent == 1:
            #     current_agent = 'B'
            # if current_agent == 2:
            #     current_agent = 'C'
            # if current_agent == 3:
            #     current_agent = 'D'
            # if current_agent == 4:
            #     current_agent = 'E'
            # if current_agent == 5:
            #     current_agent = 'F'
            # if current_agent == 6:
            #     current_agent = 'G'
            # if current_agent == 7:
            #     current_agent = 'H'
            if msg != bytes('', 'UTF-8'):
                observation = msg.decode('utf-8')
                other_agent, current_agent, author, topic, message = observation.split(",", 4)

                # The incoming message is split and added to the logfiles
                agent_log_file_name = current_agent + ".txt"
                agent_log_path = Logging.LOG_PATH / agent_log_file_name
                agent_log = open(agent_log_path.absolute(), "ab+")
                write_string = get_current_time() + ', connection from:' + other_agent + ', author:' + author + ', tag:' + topic + ',' + str(self.scenario.instant_feedback[topic]) + ' |message:' + message + '| ' + reply + '\n'
                agent_log.write(bytes(write_string, 'UTF-8'))
                agent_log.close()

                # Function call for the initialization of the trust values
                calc_trust_metrics(current_agent, observation, self.scenario)

                # Artifact finalTrust calculates the trust based on the saved values in the log file
                trust_value = final_trust(current_agent, other_agent)
                
                # Adding the trust value to the history file
                history_name = current_agent + "_history.txt"
                history_path = Logging.LOG_PATH / history_name
                history_file = open(history_path.absolute(), "ab+")
                history_file.write(bytes(get_current_time() + ', history trust value from: ' + other_agent + ' ' + str(trust_value) + '\n', 'UTF-8'))
                history_file.close()

                # Adding the trust value to the trust log
                trust_log_path = Logging.LOG_PATH / "trust_log.txt"
                trust_log = open(trust_log_path.absolute(), 'ab+')
                write_string = get_current_time() + ", agent '" + current_agent + "' trusts agent '" + other_agent + "' with value: " + trust_value + '\n'
                trust_log.write(bytes(write_string, 'UTF-8'))
                trust_log.close()
                # print("_______________________________________")
                # # print("_____________________" + trust_value + "-__________")
                #
                # if float(trust_value) < self.scenario.trust_thresholds['lower_limit']:
                #     untrustedAgents.append(other_agent)
                #     print("+++" + current_agent + ", nodes beyond redemption: " + other_agent + "+++")
                # if float(trust_value) > self.scenario.trust_thresholds['upper_limit'] or float(trust_value) > 1:
                #     self.scenario.authority.append(current_agent[2:3])
                # print("Node " + str(self.id) + " Server received data:", observation[2:-1])
                # print("_______________________________________")
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


