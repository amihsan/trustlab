from abc import ABC, abstractmethod


class BasicConnector(ABC):
    @abstractmethod
    def sums_agent_numbers(self):
        pass

    @abstractmethod
    def list_supervisors_with_free_agents(self):
        pass

    @abstractmethod
    async def reserve_agents(self, distribution, scenario_run_id, scenario_data):
        pass

    @abstractmethod
    async def start_scenario(self, distribution, scenario_run_id):
        pass

