import socket
import trustlab.lab.config as config
from trustlab.lab.connectors.channels_connector import ChannelsConnector
from trustlab.lab.distributors.greedy_distributor import GreedyDistributor
from trustlab.lab.distributors.round_robin_distributor import RoundRobinDistributor
from trustlab.serializers.scenario_serializer import ScenarioSerializer


class Director:
    def prepare_scenario(self):
        agents = self.scenario.agents
        # check if enough agents are free to work
        sums = self.connector.sums_agent_numbers()
        free_agents = sums['sum_max_agents'] - sums['sum_agents_in_use']
        if free_agents < len(agents):
            raise Exception('Currently there are not enough agents free for the chosen scenario.')
        # TODO implement scenario syntax checking (until now due to predefined scenarios not required)
        # distribute agents on supervisors
        supervisors_with_free_agents = self.connector.list_supervisors_with_free_agents()
        self.distribution = self.distributor.distribute(agents, supervisors_with_free_agents)
        # reserve agents at supervisors
        scenario_serializer = ScenarioSerializer(self.scenario)
        self.agent_host_names = self.connector.reserve_agents(self.distribution, scenario_serializer.data,
                                                              self.scenario_run_id)
        pass

    def run_scenario(self):
        pass
        # ServerStatus.set_scenario(scenario)
        # thread_server = []
        # threads_client = []
        # # creating servers
        # for n in range(len(scenario.agents)):
        #     thread_server.append(n)
        #     thread_server[n] = AgentServer(n, 2000 + int(n))
        #     thread_server[n].start()
        #
        # # logging for all Agents their trust history and their topic values if given
        # for agent in scenario.agents:
        #     history_name = agent + "_history.txt"
        #     history_path = Logging.LOG_PATH / history_name
        #     with open(history_path.absolute(), "ab+") as history_file:
        #         for other_agent, history_value in scenario.history[agent].items():
        #             history_file.write(bytes(get_current_time() + ', history trust value from: ' + other_agent + ' ' +
        #                                      str(history_value) + '\n', 'UTF-8'))
        #     topic_name = agent + "_topic.txt"
        #     topic_path = Logging.LOG_PATH / topic_name
        #     with open(topic_path.absolute(), "ab+") as topic_file:
        #         if scenario.topics and agent in scenario.topics:
        #             for other_agent, topic_dict in scenario.topics[agent].items():
        #                 if topic_dict:
        #                     for topic, topic_value in topic_dict.items():
        #                         # TODO topic not always required to be single word
        #                         topic_file.write(bytes(get_current_time() + ', topic trust value from: ' + other_agent + ' ' + topic + ' ' + str(topic_value) + '\n', 'UTF-8'))
        #
        #
        # for observation in scenario.observations:
        #     source, target, author, topic, message = observation.split(",", 4)
        #     port = 2000 + scenario.agents.index(target)
        #     client_thread = AgentClient(source, self.HOST, port, observation)
        #     threads_client.append(client_thread)
        #     client_thread.start()
        #     file_path = Logging.LOG_PATH / "director_log.txt"
        #     director_file = open(file_path.absolute(), "ab+")
        #     # write_string = get_current_time() + ", '" + source + "' sends '" + target + "' from author '" + author + "' with topic '" + topic + "' the message: " + message + '\n'
        #     write_string = get_current_time() + ", '" + source + "' sends '" + target + "', topic '" + topic + "', message: " + message + '\n'
        #     director_file.write(bytes(write_string, 'UTF-8'))
        #     director_file.close()
        #     time.sleep(1)
        # for thread in threads_client:
        #     thread.join()
        # for server in thread_server:
        #     for thread in server.threads:
        #         thread.join()
        # # ServerStatus.shutdown_server()
        # # for server in thread_server:
        # #     server.join()
        # # while len(threads_client) > 0 or any([len(server.threads) > 0 for server in thread_server]):
        # #     threads_client = [thread for thread in threads_client if thread.is_alive()]
        # return Logging.LOG_PATH / "director_log.txt", Logging.LOG_PATH / "trust_log.txt"

    def __init__(self, scenario):
        self.HOST = socket.gethostname()
        self.scenario_run_id = config.create_scenario_run_id()
        self.scenario = scenario
        self.connector = ChannelsConnector()
        if config.DISTRIBUTOR == "round_robin":
            self.distributor = RoundRobinDistributor()
        else:
            self.distributor = GreedyDistributor()
        self.distribution = None
        self.agent_host_names = None
        # Logging.new_log_path()


