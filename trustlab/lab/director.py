import time, socket
from datetime import datetime
from trustlab.models import *
from trustlab.lab.exec.AgentServer import AgentServer
from trustlab.lab.exec.AgentClient import AgentClient
from trustlab.lab.config import Logging



class Director:
    def get_current_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def runScenario(self, scenario):
        thread_server = []
        for n in range(len(scenario.agents)):
            thread_server.append(n)
            thread_server[n] = AgentServer(n, 2000 + int(n), scenario)
            thread_server[n].start()

        # with open(s, "r") as fp:
        for observation in scenario.observations:
            observation_elements = observation.split(',')
            if str(observation_elements[1]) == 'A':
                port = 2000
            if str(observation_elements[1]) == 'B':
                port = 2001
            if str(observation_elements[1]) == 'C':
                port = 2002
            if str(observation_elements[1]) == 'D':
                port = 2003
            if str(observation_elements[1]) == 'E':
                port = 2004
            if str(observation_elements[1]) == 'F':
                port = 2005
            if str(observation_elements[1]) == 'G':
                port = 2006
            if str(observation_elements[1]) == 'H':
                port = 2007
            clientthread = AgentClient(str(observation_elements[0]), self.HOST, port, str(observation_elements[0]) + ' to ' + str(observation_elements[1]) + ' author: '
                                       + str(observation_elements[2]) + ' tag: ' + str(observation_elements[3]) + ' msg: ' + str(observation_elements[4]))
            clientthread.start()
            file_path = Logging.LOG_PATH / "observerlog.txt"
            fo = open(file_path.absolute(), "ab+")
            fo.write(
                bytes(self.get_current_time() + ' Node: ', 'UTF-8') + bytes(observation_elements[1], 'UTF-8') +
                bytes(', connection from:', 'UTF-8') +
                bytes(observation_elements[0], 'UTF-8') + bytes(', author:', 'UTF-8') +
                bytes(str(observation_elements[2]), 'UTF-8') + bytes(', tag:', 'UTF-8') +
                bytes(str(observation_elements[3]), 'UTF-8') +
                bytes(',', 'UTF-8') + bytes(str(scenario.instant_feedback[observation_elements[3]]), 'UTF-8') +
                bytes(' |message:', 'UTF-8') + bytes(str(observation_elements[4]), 'UTF-8') + bytes('\n', 'UTF-8'))
            fo.close()
            time.sleep(0.1)

    def __init__(self):
        self.HOST = socket.gethostname()
        Logging.new_log_path()


