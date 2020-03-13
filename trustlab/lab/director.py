import time
import socket
from trustlab.lab.exec.AgentServer import AgentServer
from trustlab.lab.exec.AgentClient import AgentClient
from trustlab.lab.config import Logging, get_current_time, ServerStatus


class Director:
    def run_scenario(self, scenario):
        ServerStatus.set_scenario(scenario)
        thread_server = []
        threads_client = []
        # creating servers
        for n in range(len(scenario.agents)):
            thread_server.append(n)
            thread_server[n] = AgentServer(n, 2000 + int(n))
            thread_server[n].start()

        # logging for all Agents their trust history and their topic values if given
        for agent in scenario.agents:
            history_name = agent + "_history.txt"
            history_path = Logging.LOG_PATH / history_name
            with open(history_path.absolute(), "ab+") as history_file:
                for other_agent, history_value in scenario.history[agent].items():
                    history_file.write(bytes(get_current_time() + ', history trust value from: ' + other_agent + ' ' +
                                             str(history_value) + '\n', 'UTF-8'))
            topic_name = agent + "_topic.txt"
            topic_path = Logging.LOG_PATH / topic_name
            with open(topic_path.absolute(), "ab+") as topic_file:
                if scenario.topics and agent in scenario.topics:
                    for other_agent, topic_dict in scenario.topics[agent].items():
                        if topic_dict:
                            for topic, topic_value in topic_dict.items():
                                # TODO topic not always required to be single word
                                topic_file.write(bytes(get_current_time() + ', topic trust value from: ' + other_agent + ' ' + topic + ' ' + str(topic_value) + '\n', 'UTF-8'))


        for observation in scenario.observations:
            source, target, author, topic, message = observation.split(",", 4)
            port = 2000 + scenario.agents.index(target)
            client_thread = AgentClient(source, self.HOST, port, observation)
            threads_client.append(client_thread)
            client_thread.start()
            file_path = Logging.LOG_PATH / "director_log.txt"
            director_file = open(file_path.absolute(), "ab+")
            write_string = get_current_time() + ", '" + source + "' will send to '" + target + "' from author '" + author + "' with topic '" + topic + "' the message: " + message + '\n'
            director_file.write(bytes(write_string, 'UTF-8'))
            director_file.close()
            time.sleep(1)
        for thread in threads_client:
            thread.join()
        for server in thread_server:
            for thread in server.threads:
                thread.join()
        # ServerStatus.shutdown_server()
        # for server in thread_server:
        #     server.join()
        # while len(threads_client) > 0 or any([len(server.threads) > 0 for server in thread_server]):
        #     threads_client = [thread for thread in threads_client if thread.is_alive()]
        return Logging.LOG_PATH / "director_log.txt", Logging.LOG_PATH / "trust_log.txt"

    def __init__(self):
        self.HOST = socket.gethostname()
        Logging.new_log_path()


