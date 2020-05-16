from abc import ABC, abstractmethod


class BasicConnector(ABC):
    @abstractmethod
    def sums_agent_numbers(self):
        pass

    @abstractmethod
    def list_supervisors_with_free_agents(self):
        pass

    @abstractmethod
    def reserve_agents(self, distribution):
        pass