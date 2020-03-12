import time, socket
from datetime import datetime
from trustlab.models import *
from trustlab.lab.exec.AgentServer import AgentServer
from trustlab.lab.exec.AgentClient import AgentClient
from trustlab.lab.config import Logging, get_current_time


class Director:
    def run_scenario(self, scenario):
        thread_server = []
        threads_client = []
        # creating servers
        for n in range(len(scenario.agents)):
            thread_server.append(n)
            thread_server[n] = AgentServer(n, 2000 + int(n), scenario)
            thread_server[n].start()

        # logging for all Agents their trust history
        for agent in scenario.agents:
            history_name = agent + "_history.txt"
            history_path = Logging.LOG_PATH / history_name
            for other_agent, history_value in scenario.history[agent].items():
                director_file = open(history_path.absolute(), "ab+")
                director_file.write(bytes(get_current_time() + ', history trust value from: ' + other_agent + ' ' +
                                         str(history_value) + '\n', 'UTF-8'))
                director_file.close()

        for observation in scenario.observations:
            source, target, author, topic, message = observation.split(",", 4)
            port = 2000 + scenario.agents.index(target)
            client_thread = AgentClient(source, self.HOST, port, observation)
            threads_client.append(client_thread)
            client_thread.start()
            file_path = Logging.LOG_PATH / "director_log.txt"
            director_file = open(file_path.absolute(), "ab+")
            write_string = get_current_time() + ", '" + source + "' will send to '" + target + "' from author: '" + author + "' with topic: " + topic + "," + " the message: " + message + '\n'
            director_file.write(bytes(write_string, 'UTF-8'))
            director_file.close()
            time.sleep(1)
        for thread in threads_client:
            thread.join()
        for server in thread_server:
            for thread in server.threads:
                thread.join()
        # while len(threads_client) > 0 or any([len(server.threads) > 0 for server in thread_server]):
        #     threads_client = [thread for thread in threads_client if thread.is_alive()]
        return Logging.LOG_PATH / "director_log.txt", Logging.LOG_PATH / "trust_log.txt"

    def __init__(self):
        self.HOST = socket.gethostname()
        Logging.new_log_path()


