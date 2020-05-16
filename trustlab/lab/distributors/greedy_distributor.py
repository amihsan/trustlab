from trustlab.lab.distributors.basic_distributor import BasicDistributor


class GreedyDistributor(BasicDistributor):
    def distribute(self, agents, supervisors):
        distribution = {}
        while len(agents) > 0:
            free_agents = supervisors[0].max_agents - supervisors[0].agents_in_use
            distribution[supervisors[0].channel_name] = agents[:free_agents]
            agents = agents[free_agents:]
            supervisors = supervisors[1:]
        return distribution

