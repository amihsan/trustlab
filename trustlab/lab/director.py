import socket
import trustlab.lab.config as config
from trustlab.lab.connectors.channels_connector import ChannelsConnector
from trustlab.lab.distributors.greedy_distributor import GreedyDistributor
from trustlab.lab.distributors.round_robin_distributor import RoundRobinDistributor
from trustlab.serializers.scenario_serializer import ScenarioSerializer


class Director:
    async def prepare_scenario(self):
        agents = self.scenario.agents
        # check if enough agents are free to work
        sums = await self.connector.sums_agent_numbers()
        free_agents = sums['sum_max_agents'] - sums['sum_agents_in_use']
        if free_agents < len(agents):
            raise Exception('Currently there are not enough agents free for the chosen scenario.')
        # TODO implement scenario syntax checking (until now not required due to predefined scenarios only)
        # distribute agents on supervisors
        supervisors_with_free_agents = await self.connector.list_supervisors_with_free_agents()
        self.distribution = await self.distributor.distribute(agents, supervisors_with_free_agents)
        # reserve agents at supervisors
        scenario_serializer = ScenarioSerializer(self.scenario)
        self.discovery = await self.connector.reserve_agents(self.distribution, self.scenario_run_id,
                                                             scenario_serializer.data)
        print(self.discovery)

    async def run_scenario(self):
        await self.connector.start_scenario(self.distribution.keys(), self.scenario_run_id)
        scenario_runs = True
        while scenario_runs:
            done_dict = await self.connector.get_next_finished_observation()


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
        self.discovery = None
        # Logging.new_log_path()


